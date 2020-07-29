# import os
# import tensorflow as tf
# from tensorflow import keras

# # Define a simple sequential model
# def create_model():
#   model = tf.keras.models.Sequential([
#     keras.layers.Dense(512, activation='relu', input_shape=(784,)),
#     keras.layers.Dropout(0.2),
#     keras.layers.Dense(10)
#   ])

#   model.compile(optimizer='adam',
#                 loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
#                 metrics=['accuracy'])

#   return model

# # Create a basic model instance
# model = create_model()

# model = model.load_weights("../pred/predictor/tf_model.h5")

# print(model)

# model.predict(['şerefsiz'])
# model.predict(['selam'])

import ktrain
import pandas as pd
import re

model = ktrain.load_predictor("../pred/predictor/")

print(model.predict(['asd']))

print(model.predict(['asd2']))
