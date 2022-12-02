#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
working_directory = os.getcwd()
print(working_directory)
import datetime


# In[7]:


#loaded the file in dataframe

df = pd.read_csv(r'/Users/mp/Downloads/taxis.csv')
print(df.info())
df.head()


# In[8]:


#checking for null values
#to check percentage of null
(df.isnull().sum()/len(df))*100

#df.isnull().sum()


# In[9]:



# Remove all duplicate rows
df.drop_duplicates(keep=False)


# In[10]:


#to check outlier 

df_to_plot = df.select_dtypes(include=np.number)
df_to_plot.plot(subplots=True, layout=(4,4), kind='box', figsize=(12,14), patch_artist=True)
plt.subplots_adjust(wspace=0.5);


# In[11]:


# to check total number of passengers who took trip
sns.countplot(x='passengers', data=df)


# In[13]:


#to check passengers basis Payment
sns.countplot(x='payment', hue='passengers', data=df)


# In[16]:


# to check fare contibution by passengers
sns.boxplot(x='passengers',y='fare', data=df)


# In[23]:


# to check pickup points
sns.countplot(x='pickup_borough', data=df)


# In[24]:


# to check dropoff points
sns.countplot(x='dropoff_borough', data=df)


# In[26]:


to check fare distribution across distance
sns.boxplot(x='distance',y='fare', data=df)


# In[27]:


#to check the fare distribution Overall
sns.histplot(df['fare'])


# In[34]:


#to convert date-time to numerical format
df['pickup']=pd.to_datetime(df['pickup'])
df['dropoff']=pd.to_datetime(df['dropoff'])


# In[35]:


#dates conversion to day of the week
df['pickup_day']=df['pickup'].dt.day_name()
df['dropoff_day']=df['dropoff'].dt.day_name()


# In[36]:


# plot of pickup day of the week
sns.countplot(x='pickup_day', data=df)


# In[37]:


# plot of dropoff day of the week
sns.countplot(x='dropoff_day', data=df)


# In[38]:


#it is difficult to analyze time partas it is represented in hr-min-sec format hence we created 4 timezones
#morning (04-10 hrs), Midday (10-16 hrs), evening( 16-22 hrs), latenight(22-04 hrs). 

def timezone(x):
    if x>=datetime.time(4, 0, 1) and x <=datetime.time(10, 0, 0):
        return 'morning'
    elif x>=datetime.time(10, 0, 1) and x <=datetime.time(16, 0, 0):
        return 'midday'
    elif x>=datetime.time(16, 0, 1) and x <=datetime.time(22, 0, 0):
        return 'evening'
    elif x>=datetime.time(22, 0, 1) or x <=datetime.time(4, 0, 0):
        return 'late night'


# In[43]:


#created new column for morning (04-10 hrs), Midday (10-16 hrs), evening( 16-22 hrs), latenight(22-04 hrs) as Timezone
df['pickup_timezone']=df['pickup'].apply(lambda x :timezone(datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").time()) )
df['dropoff_timezone']=df['dropoff'].apply(lambda x :timezone(datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").time()) )


# In[44]:


# plotted that column 
sns.countplot(x='pickup_timezone', data=df)


# In[45]:


# plotted that column 
sns.countplot(x='dropoff_timezone', data=df)


# In[48]:


# to create new column for hours
df['pickup_hour']=df['pickup'].dt.hour
df['dropoff_hour']=df['dropoff'].dt.hour


# In[51]:


#plotted hours.
sns.histplot(x='pickup_hour',data=df) 


# In[52]:


#to see frequency distribution
sns.histplot(x='dropoff_hour',data=df) 


# In[53]:


#to find correlation between metrics.
dataplot=sns.heatmap(df.corr())
plt.show()


# In[59]:


# to see distribution basis tip and payment.
sns.boxplot(x='tip',y='payment', data=df)


# In[65]:


#to see payment method used on days of the week
sns.countplot(x='pickup_day',hue='payment',data=df)


# In[66]:



sns.heatmap(df.isnull(),yticklabels= False, cbar= False, cmap= 'viridis')


# In[ ]:




