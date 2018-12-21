#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import keras
import numpy as np
from keras.models import load_model
import json
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform


# In[2]:

def predict(x):
    keras.backend.clear_session()
    with open("model_data/regression_model.json","r") as data:
        model_json = json.load(data) 


    # In[3]:


    with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        model = keras.models.model_from_json(model_json)


    # In[7]:
    x = np.array([x])

    model.load_weights("model_data/regression_weights")


    # In[5]:


    #has to be in this format 
    #x = np.array([[-0.39805957, -0.48028321,  0.41150996, -0.26091209, -1.01875102,
    #         -0.68907594, -0.37316522,  1.22683341, -0.63105852, -0.70158051,
    #         -1.17261374,  0.45007505,  0.44124745]])


    # In[8]:


    return(model.predict(x)[0,0])



    # In[ ]:




