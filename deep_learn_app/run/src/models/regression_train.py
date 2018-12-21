#!/usr/bin/env python3

from __future__ import absolute_import, division, print_function
import tensorflow as tf
from tensorflow import keras
import numpy as np
import json


# In[94]:

def train():
  keras.backend.clear_session()
  with open("data/data.json","r") as data:
      data = json.load(data)
  # Shuffle the training set
  inputs,outputs= np.array(data['inputs']),np.array(data['outputs'])
  aa = int(len(inputs)*.9)
  train_inputs,train_outputs=inputs[:aa],outputs[:aa] 
  test_inputs,test_outputs=inputs[aa:],outputs[aa:] 
  order = np.argsort(np.random.random(train_outputs.shape))
  train_inputs = train_inputs[order]
  train_outputs = train_outputs[order]


  # In[95]:


  mean = train_inputs.mean(axis=0)
  std = train_inputs.std(axis=0)
  train_inputs = (train_inputs - mean) / std
  test_inputs = (test_inputs - mean) / std


  # In[96]:


  def build_model():
    model = keras.Sequential([
      keras.layers.Dense(64, activation=tf.nn.relu,
                        input_shape=(train_inputs.shape[1],)),
      keras.layers.Dense(64, activation=tf.nn.relu),
      keras.layers.Dense(1)
    ])

    optimizer = tf.train.RMSPropOptimizer(0.001)

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae'])
    return model

  model = build_model()


  # In[97]:


  EPOCHS = 500


  # In[98]:


  # The patience parameter is the amount of epochs to check for improvement
  early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)
  history = model.fit(train_inputs, train_outputs, epochs=EPOCHS,
                      validation_split=0.2, verbose=0,
                      callbacks=[early_stop])


  # In[99]:


  model_trained = model.to_json()


  # In[100]:


  with open('model_data/regression_model.json',"w") as file:
      json.dump(model_trained,file)


  # In[101]:


  model.save_weights("model_data/regression_weights",save_format="h5")

