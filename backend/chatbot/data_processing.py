import json
import os

import nltk
from nltk.stem.lancaster import LancasterStemmer

import pickle
import numpy as np

stemmer = LancasterStemmer()

def load_traning_data():
    return json.loads(open('backend/chatbot/utilities/conversation.json').read())

def save_data(training_data, output_data, labels):
    pickle.dump(labels, open("backend/chatbot/utilities/labels_words.pickle", "wb"))
    pickle.dump(training_data, open("backend/chatbot/utilities/training_data.pickle", "wb"))
    pickle.dump(output_data, open("backend/chatbot/utilities/output_data.pickle", "wb"))

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

    words = sorted(list(set(words)))
    labels = sorted(labels)

    return words, labels

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

