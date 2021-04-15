#!/usr/bin/env python
# coding: utf-8

# # Ejercicio 7
# Paula Valentina Bonilla Hernández
# Pablo Felipe Rengifo Montilla 

# In[337]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import *
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('classic')


# In[338]:


df = pd.read_csv("https://raw.githubusercontent.com/diegour1/LabMetodosComputacionales/main/DataFiles/world_pop.csv")


# In[339]:


pd.set_option("display.precision", 10)
pd.set_option("display.max.columns", 10)
df.head(471)


# In[340]:


dat = []
p = 0
x = np.array(df['Year'])
y = np.array(df['World Population'])     


# In[341]:


h = []
g = []
for i in range(len(x)):
    if x[i]>=700 and x[i]<=1900:
        h.append(x[i])
        g.append(y[i])
print (h,g)


# In[342]:


#arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
#indices = np.where(arr<=3)
#arr = np.delete(arr, indices)


# In[343]:


h.sort()
g.sort()


# In[344]:


model = np.polyfit(h,g,10)
x=np.linspace(1,100,100)
plt.plot(h,g,'+')
plt.plot(h,polyval(model,h))
plt.title('Ajuste polinomial')
plt.xlabel(r'$Población$')
plt.ylabel(r'$Años$')
plt.savefig("BonillaPaulaRengifoPablo")
plt.show()


# In[345]:


c = np.polyfit(h,g,4)
print(f"coeffs 4to grado = {c}")


# In[ ]:





# In[ ]:




