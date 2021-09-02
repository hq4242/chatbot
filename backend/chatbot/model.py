import tensorflow
from tensorflow import keras 

from keras import Sequential
from keras import layers
from keras.layers import Dense, Input, Flatten
from keras.utils import to_categorical

import numpy as np
import pickle #para codificar la conversacion

def load_pickled_data(): #Crear ficheros para guardar las salidas en binario
    data_x = pickle.load(open("backend/chatbot/utilities/training_data.pickle", "rb")) 
    #para cargar los datos del fichero d|e forma binaria con los permisos de rb(leer binario)
    data_y = pickle.load(open("backend/chatbot/utilities/output_data.pickle", "rb"))
    #para cargar los datos del fichero de forma binaria con los permisos de rb(leer binario)

    return data_x, data_y #Retorna los ficheros

def training_model(): #modelamiento de formacion
    data_x, data_y = load_pickled_data() 

    #Creando el modelo definiremos la estructura de los datos almacenados para clasificar
    model = Sequential() #Para obtenet multiples entradas
    model.add(Dense(16, input_shape=(len(data_x[0]),))) 
    ''' ingreso de datos del modelo segun 
    su peso donde 0 toma referencia a la primera cadena '''
    model.add(Dense(32, activation='relu')) #funcion de activacion
    model.add(Dense(32, activation='relu')) #funcion de activacion
    model.add(Dense(len(data_y[0]), activation='softmax'))#activation='softmax Convierte el vector de numeros a probabilidades

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    ''' optimizer=adam metodo para optimizar el modelo es un metodo de decenso, loss='categorical_crossentropy' 
    calcula la cantidad que debe buscar en el modelo para minimizar durante el entrenamiento, metrics=['accuracy'] 
    Para calcular la precicion del subconjuntomodel.fit(data_x, data_y, epochs=128)#fit entrena el modelo en 128 epocas'''

    model.save("backend/chatbot/utilities/model.h5")#guarda la sintetizacion del modelo.

