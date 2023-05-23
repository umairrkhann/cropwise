#!/usr/bin/env python
# coding: utf-8

# In[4]:


from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


# In[6]:


dataset = pd.read_csv('Downloads/Crop_recommendation.csv')


# In[61]:


X= dataset[["N","P","K","temperature","humidity","ph","rainfall"]]
Y= dataset[["label"]]


# In[62]:


X.head()


# In[63]:


a = Y['label'].unique()
#Y.replace("rice", 1, inplace=True)a
i = 0
for x in a :
    Y.replace(x, i, inplace=True)
    i+=1


# In[64]:


Y


# In[65]:


#split data into train and test sets
seed = 7
test_size = 0.2
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)


# In[66]:


# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)


# In[67]:


# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)


# In[68]:


# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]


# In[71]:


# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))


# In[ ]:




