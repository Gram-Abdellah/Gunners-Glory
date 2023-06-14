#!/usr/bin/env python
# coding: utf-8

# In[31]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[56]:


url=('https://theathletic.com/football/team/arsenal/stats/')
response = requests.get(url)
table_data = pd.read_html(response.text)
Players = table_data[1]
GKs = table_data[0]
print(table)
Players.to_csv(r'\Arsenal 2023\Players.csv')
GKs.to_csv(r'\GoalKappers.csv')


# In[59]:


rslt = requests.get('https://www.footballcritic.com/arsenal-fc/formations/467')
table_data = pd.read_html(rslt.text)
Games = table_data[0]
print(Games)
Players.to_csv(r'\Arsenal 2023\Games.csv')


# In[ ]:





# In[ ]:




