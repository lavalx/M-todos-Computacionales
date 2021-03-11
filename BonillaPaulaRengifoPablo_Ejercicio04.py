#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
import numpy as np
from numpy import random
from random import randint


# In[46]:


d1 = randint(1, 6)
d2 = randint(1, 6)
d3 = randint(1, 6)
print (d1, d2, d3)


# In[47]:


def winAlice(n):
    for i in range(n):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        d3 = randint(1, 6)
        if d1 == d1 == d3:
            numIguales = 1
    prob_same = numIguales/n
    
    return prob_same     


# In[48]:


def winBob(n):
    for i in range(n):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        d3 = randint(1, 6)
        dados = [d1,d2,d3]
        dados.sort()
        if dados[0] == dados[1] - 1 and dados[1] == dados[2] - 1:
            numConsecu = 1
        
    prob_consecutive = numConsecu/n
    
    return prob_consecutive


# In[49]:


print('la probabilidad que Alice gane es de', winAlice(10000)*100,'%',' Y la probabilidad que Bob gane es de', winBob(10000)*100, '%')   


# In[ ]:




