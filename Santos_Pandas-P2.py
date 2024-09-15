#!/usr/bin/env python
# coding: utf-8

# # Problem 2

# In[9]:


import pandas as pd


# In[5]:


#Loading the downloaded file in phyton
cars = pd.read_csv('cars.csv')
cars


# In[12]:


#Printing the first five odd rows
cars.iloc[1::2].head()


# In[14]:


#Display the row that contains the ‘Model’ of ‘Mazda RX4’
cars.loc[(cars['Model']=='Mazda RX4'), ['Model']]


# In[16]:


#Displaying the 'cyl' of the car model 'Camaro Z28'
cars.loc[[23],['Model', 'cyl']]


# In[18]:


#Printing the 'cyl' and 'gear' of the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’.
cars.loc[[1, 18, 28],['Model', 'cyl', 'gear']]


# In[ ]:




