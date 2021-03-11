#!/usr/bin/env python
# coding: utf-8

# # Laboratorio 5 - Métodos Computacionales 
# Paula Valentina Bonilla Hernández
# 
# Pablo Felipe Rengifo Montilla

# In[42]:


from __future__ import print_function, division
import numpy as np
import scipy.special
import pylab as plt


# In[43]:


N = 10000000


# In[44]:


for D in np.arange(10,11):

    all = np.random.uniform(-1,1, D*N).reshape(N,D) # Esto para generar puntos en el cubo

    fadentro = Ninside/N #Fracción de puntos dentro de la esfera
    cubo = 2**D # Volumen del cubo (de -1 a 1)
    volumen_sphere_10d = fadentro * cubo # Volumen de la esfera
    

    print(f"Volumen esfera en 10D = {volumen_sphere_10d}")


# In[ ]:




