#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
from math import *


# In[23]:


# capítulo 2.1 del libro 
C = -20
dC = 5
while C <= 40:
    F = (9.0/5)*C + 32
    print (C, F)
    C = C + dC


# In[24]:


# capítulo 2.14 del libro = listas 
C1 = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
C1.append(35) #Un nuevo elemento 35 se agrega al final de la lista
print (C1)
C1 = C1 + [40,45] #Se extiende C1 al final con 40, 45.
print (C1)
C1.insert(0,15) #se inserta un nuevo elemento -15 en el indice 0
print (C1)
del C1[2] #Se elimina un elemento del indice 2 (3er elemento)
print (C1) 
print ("el largo de la lista es ",len (C1)) #retorna el lenght de una lista
print ("El indice del elemento 15 es",C1.index(15)) #busca el indice de el elemento 15


# In[26]:


# capítulo 2.15 del libro = listas en loops 
grados = [0, 10, 20, 40, 100]
for C in grados:
    print ("elementos de la lista:", C)
print ("la lista de los grados tiene", len (grados), "elementos")


# In[28]:


#vamos a crear una tabla donde guardemos todos los grados celcius y luego usar un loop para volverlos F
Cgrados = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
for C in Cgrados:
    F = (9.0/5)*C +32
    print (C, F)

#Pero este formato imprime algo horrible, no parece una tabla de verdad
#Un buen formato se obtiene forzando C y F a escribirse en campos de un ancho en especifico
Cgrados = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
for C in Cgrados:
    F = (9.0/5)*C +32
    print  ’%5d %5.1f’ % (C, F)


# In[ ]:




