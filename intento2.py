#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
from math import *
import matplotlib.pyplot as plt


# In[50]:


def f(x):
    return (x+2)*(x-2)*(x-4) 

def bisec(f, a, b):
    error = 10
    while error > 1e-8:
        c = (a + b) / 2
        fa = f(a)
        fc = f(c)
        if fc == 0:
            root = c
            break
        elif fa * fc < 0: 
            b = c
        else:
            a = c
        root = c
        error = abs(fc)

print (raiz)

def root(f, a, b):
    e = 0.001
    while (b - a) > e:
        a,b = bisec(f,a,b)

    return a 


# In[51]:


x = np.linspace(-3, 4, 101)
plt.plot(x, f(x))
plt.grid()
plt.show()


# In[ ]:





# In[6]:





        


# In[ ]:




