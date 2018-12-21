#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import json


# In[2]:

def labels():
    with open("data/data.json","r") as data:
        data = json.load(data)
    labels = np.array(data['labels'])
    return labels.tolist()


# In[10]:





# In[ ]:




