#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
from math import *


# In[8]:


# f -- función
# a -- inicio intervalo
# b -- fin intervalo

def f(x):
    return (x+2)(x-2)(x-4)



def bisec(f, a, b):
    m = ( a +b ) / 2
    if f(m) * f(b) < 0:
        a = m
        b = b

    else:
        a = a
        b = b
        
    return a,b




def root(f, a, b):
    e = 0.001
    while (b - a) > e:
        a,b = bisec(f,a,b)
    return a 


# In[9]:


print (root)


# In[ ]:




