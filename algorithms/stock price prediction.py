#!/usr/bin/env python
# coding: utf-8

# In[2]:


import quandl, math
import numpy as np
import pandas as pd
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime


# In[3]:


style.use('ggplot')


# In[4]:


df=quandl.get("WIKI/GOOGL")
print(df)
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High']-df['Adj. Low']) / df['Adj. Close']*100.0
df['PCT_change']=(df['Adj. Close']-df['Adj. Open']) / df['Adj. Open']*100.0


# In[4]:


df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
forecast_col='Adj. Close'
df.fillna(value=-99999, inplace=True)
forecast_out=int(math.ceil(0.01*len(df)))
df['label']=df[forecast_col].shift(-forecast_out)


# In[5]:


x=np.array(df.drop(['label'],1))
x=preprocessing.scale(x)
x_lately=x[-forecast_out:]  #y
x=x[:-forecast_out]         #x


# In[6]:


print(x)


# In[7]:


print(x_lately)


# In[8]:


df.dropna(inplace=True)
y=np.array(df['label'])
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.2)
clf=LinearRegression(n_jobs=-1)
clf.fit(x_train,y_train)
confidence=clf.score(x_test,y_test)


# In[9]:


forecast_set=clf.predict(x_lately)
df['Forecast']=np.nan


# In[10]:


last_date=df.iloc[-1].name
last_unix=last_date.timestamp()
one_day=86400
next_unix=last_unix+one_day


# In[11]:


for i in forecast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix+=86400
    df.loc[next_date]=[np.nan for _ in range(len(df.columns)-1)]+[i]


# In[12]:


df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

