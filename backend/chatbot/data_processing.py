import json
import os

import nltk
from nltk.stem.lancaster import LancasterStemmer

import pickle
import numpy as np

stemmer = LancasterStemmer()

def load_traning_data():#Cargaremos los datos entrenados
    return json.loads(open('backend/chatbot/utilities/conversation.json').read())#llamar el archivo de datos entrenados

def save_data(training_data, output_data, labels):#funcion para abrir, asignar entradas y salidas de ficheros
    pickle.dump(labels, open("backend/chatbot/utilities/labels_words.pickle", "wb"))#abrir archivo donde se codificara en forma binaria
    pickle.dump(training_data, open("backend/chatbot/utilities/training_data.pickle", "wb"))
    pickle.dump(output_data, open("backend/chatbot/utilities/output_data.pickle", "wb"))

#Esta es la arquitectura para convertir de binaria palabras
def convert_ml_data(docs_x, docs_y, labels, words):
    training_data = []
    output_data = []
    out_empty = [0 for _ in range(len(labels))]

    for k, doc in enumerate(docs_x):
        all_words = []
        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if(w in wrds):
                all_words.append(1)
            else:
                all_words.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[k])] = 1

        training_data.append(all_words)
        output_data.append(output_row)

    training_data = np.array(training_data)
    output_data = np.array(output_data)

    return training_data, output_data

def modifing_words(words, labels):
    words = [stemmer.stem(w.lower()) for w in words if w != "?"]

    #Para liminamos todas las palabras dobles
    words = sorted(list(set(words)))
    labels = sorted(labels)

    return words, labels

#funcion para el tratamiento de las palabras del modelo en este caso conversation.json
def processing_the_dataset():
    data = load_traning_data()

    words, labels = [], []
    docs_x, docs_y = [], []

    for conversation in data['conversation']:
        for pattern in conversation['patterns']:
            tokenized_word = nltk.word_tokenize(pattern)
            words.extend(tokenized_word)

            docs_x.append(tokenized_word)
            docs_y.append(conversation["tag"])
            
        if conversation['tag'] not in labels:
            labels.append(conversation['tag'])

    words, labels = modifing_words(words, labels)
    training_data, output_data = convert_ml_data(docs_x, docs_y, labels, words)

    save_data(training_data, output_data, [labels, words])

