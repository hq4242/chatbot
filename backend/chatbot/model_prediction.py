import tensorflow
import tensorflow.keras
from tensorflow.keras import models

import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer

import pickle
import json
import random

from chatbot.data_processing import processing_the_dataset
from chatbot.model import training_model

stemmer = LancasterStemmer()

TRAIN_MODEL = 0
NO_MODEL = 0

if(TRAIN_MODEL):
    processing_the_dataset()
    training_model()

try:
    data = json.loads(open('/usr/src/chatbot/utilities/conversation.json').read())["conversation"]
    model = models.load_model("/usr/src/chatbot/utilities/model.h5")
    labels, words = pickle.load(open('/usr/src/chatbot/utilities/labels_words.pickle' ,'rb'))
except:
    NO_MODEL = 1

def modifing_sentence(sentence, words):
    all_words = [0 for _ in range(len(words))]

    mod_words = nltk.word_tokenize(sentence)
    mod_words = [stemmer.stem(word.lower()) for word in mod_words]

    for se in mod_words:
        for i, w in enumerate(words):
            if(w == se):
                all_words[i] = 1
            
    return np.array([all_words])

def predict(sentence):
    if(NO_MODEL):
        print("Error: Necesitas entrenar el modelo.")
        exit()

    data_x = modifing_sentence(sentence, words)
    prediction = model.predict(data_x)
    tag = labels[np.argmax(prediction)]

    for tags in data:
            if tags['tag'] == tag:
                answer = tags['responses']

    return random.choice(answer)

