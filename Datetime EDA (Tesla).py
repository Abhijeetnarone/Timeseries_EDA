#!/usr/bin/env python
# coding: utf-8

# In[34]:


##  Install pandasw data reader 
get_ipython().system('pip install pandas-datareader')


# In[35]:


import pandas_datareader as pdr
import pandas as pd
from datetime import datetime


# In[4]:


df_tesla = pdr.get_data_yahoo('TSLA')


# In[38]:


type(df_tesla)


# In[37]:


df_tesla.head()


# In[7]:


df_tesla.tail()


# In[45]:


df_tesla['High'].plot(figsize=(12,4))


# In[46]:


## X limit and Y limit
df_tesla['High'].plot(xlim=['2020-01-01','2021-09-01'],figsize=(12,4))


# In[47]:


df_tesla['High'].plot(xlim=['2020-01-01','2021-09-01'],ylim=[0,900],figsize=(12,4))


# In[48]:


## X limit and Y limit and coloring
df_tesla['High'].plot(xlim=['2020-01-01','2021-09-01'],ylim=[0,900],figsize=(12,4),ls='--', c='Red')


# In[49]:


df_tesla.index


# In[50]:


index=df_tesla.loc['2020-01-01':'2021-09-01'].index
share_open=df_tesla.loc['2020-01-01':'2021-09-01']['Open']


# In[51]:


share_open


# In[52]:


index


# In[53]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[54]:


figure,axis=plt.subplots()
plt.tight_layout()
##preventing overlapoing
figure.autofmt_xdate()
axis.plot(index,share_open)


# In[55]:


## DateTime index


# In[59]:


df_tesla=df_tesla.reset_index()


# In[61]:


df_tesla.info()


# In[65]:


df_tesla=df_tesla.set_index('Date',drop=True)


# In[66]:


df_tesla.head()


# In[67]:


## datetime
from datetime import datetime


# In[69]:


datetime(2021,11,21)


# In[70]:


datetime.now()


# In[74]:


date=datetime(2021,11,21)


# In[75]:


date


# In[76]:


date.date()


# In[77]:


date.day


# In[78]:


date.weekday()


# In[80]:


date.year


# In[81]:


date.month


# ## Time resampling

# In[83]:


df_tesla.head()


# In[85]:


df_tesla.resample(rule='A').min()


# In[86]:


df_tesla.resample(rule='A').max()


# In[88]:


## year end frequancy
df_tesla.resample(rule='A').max()['Open'].plot()


# In[90]:


## quarterly start frequancy
df_tesla.resample(rule='QS').max()['High'].plot()


# In[92]:


## Business End frequancy
df_tesla.resample(rule='BA').max()


# In[93]:


## quarterly quarters frequancy
df_tesla.resample(rule='BQS').max()


# In[95]:


## Ploting
df_tesla['Open'].resample(rule='A').max().plot(kind='bar')


# In[100]:


df_tesla['Open'].resample(rule='M').max().plot(kind='bar',figsize=(15,6))


# In[111]:


df_tesla['High'].rolling(10).mean().head(20)


# In[110]:


df_tesla.head()


# In[112]:


df_tesla['Open:30 days rolling']=df_tesla['Open'].rolling(30).mean()


# In[114]:


df_tesla.head(32)


# In[117]:


df_tesla[['Open','Open:30 days rolling']].plot(figsize=(12,5))


# In[ ]:




