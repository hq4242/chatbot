import tensorflow
from tensorflow import keras

from keras import Sequential
from keras import layers
from keras.layers import Dense, Input, Flatten
from keras.utils import to_categorical

import numpy as np
import pickle

def load_pickled_data():
    data_x = pickle.load(open("backend/chatbot/utilities/training_data.pickle", "rb"))
    data_y = pickle.load(open("backend/chatbot/utilities/output_data.pickle", "rb"))

    return data_x, data_y

def training_model():
    data_x, data_y = load_pickled_data()

    # Creating the model
    model = Sequential()
    model.add(Dense(16, input_shape=(len(data_x[0]),)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(data_y[0]), activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(data_x, data_y, epochs=128)

    model.save("backend/chatbot/utilities/model.h5")

