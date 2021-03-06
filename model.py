# -*- coding: utf-8 -*-
"""Stock - Reliance Predicition .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LI5v3zGim5kOW8nTsl8_ZlCMque7FM4Y
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle



import yfinance as yf

dataset = yf.download('RELIANCE.NS', start='2020-01-01')

dataset.head()

dataset.drop(['Adj Close', 'Volume'], axis=1, inplace=True)

dataset.isna().any()

dataset['Open'].plot(figsize=(16,6))

cor = dataset.corr()
cor

import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(cor, annot=True)

dataset.describe()

from scipy.stats import zscore

zscore(dataset)

X = dataset.drop('Close', axis=1)

Y = dataset['Close']

dataset['Close: 30 Day Mean'] = dataset['Close'].rolling(window=30).mean()
dataset[['Close','Close: 30 Day Mean']].plot(figsize=(16,6))

# Optional specify a minimum number of periods
dataset['Close'].expanding(min_periods=1).mean().plot(figsize=(16,6))

#split data
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(X,Y, test_size=0.30)

xtrain.shape

from sklearn.linear_model import LinearRegression

#Build Model
model = LinearRegression()

#train the model
model.fit(xtrain, ytrain)

#Predict
Yp = model.predict(xtest)

Yp

#Identify a, b values
model.intercept_

model.coef_

#Test the model
model.score(xtrain, ytrain)

model.score(xtest, ytest)

#Evaluate the Model
from sklearn.metrics import mean_squared_error

mean_squared_error(Yp, ytest)

pickle.dump(model, open('model.pkl', 'wb'))

model2 = pickle.load(open('model.pkl', 'rb'))

model2.score(xtrain, ytrain)