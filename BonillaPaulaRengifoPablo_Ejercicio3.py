#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from math import *
import matplotlib.pyplot as plt


# In[6]:


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
   return root



def raiz(f, a, b):
   e = 0.001
   while (b - a) > e:
       a,b = bisec(f,a,b)

   return a 


# In[7]:


x = np.linspace(-3, 4, 101)
plt.plot(x, f(x))
plt.grid()
plt.show()


# In[19]:


def f(x):
    return (x+2)*(x-2)*(x-4)
lista = []
i = 0
while i <=3:
    if (i == 0):
        lista.insert(0,bisec(f, -3, -1)) 
    if (i == 1):
        lista.insert(1,bisec(f, 1, 3)) 
    if (i == 2):
        lista.insert(2,bisec(f, 3, 5))
    i += 1 

print("las raices de la funcion son",lista)


# In[ ]:




