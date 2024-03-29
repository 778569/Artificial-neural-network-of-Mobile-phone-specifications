# -*- coding: utf-8 -*-
"""Mobile phone specification_ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gOrCx3M2YZA-oSSFcvVoAX2yD4UbxFPf
"""

import pandas as pd
dataset = pd.read_csv("Mobile_Price_Classification-220531-204702.csv")
dataset.head(5)

# Variables 20
# Split dependence and independence variable
# Indepentant variable = X
# Dependent variable = Y


x = dataset.drop(['price_range'], axis = 1)
y = dataset['price_range']
print(Y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(x_train.shape[1],)),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # For binary classification
])
model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train,validation_data=(x_test, y_test), epochs=100, batch_size=32)

model.save_weights('model_weights.h5')