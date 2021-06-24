#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
# initialize list of lists
data=[["ayo", 10], ["Imran", 15], ["chucks", 14]]

# create the pandas dataframe from the list and adding column headers
df=pd.DataFrame(data, columns= ["name", "Age"])

#print dataframe
print(df)


# In[15]:


data={"name": ["ayo", "imran","chucks"], "age":[10,15,14]}
df=pd.DataFrame(data)
df


# 
#           

# In[19]:


csv_df=pd.read_csv("desktop/Data_2006.csv")
csv_df


# In[ ]:





# In[ ]:




