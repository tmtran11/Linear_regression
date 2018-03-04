# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:46:32 2018
First linear Regression
@author: FPTShop
"""

import numpy as np
from matplotlib import pyplot as plt
X = []
Y = []
for line in open('data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))
    
X = np.array(X)
Y = np.array(Y)
plt.scatter(X,Y)
plt.show()

denominator = X.dot(X) - X.mean()*X.sum()
a = (Y.dot(X)-Y.mean()*X.sum())/denominator
b = (Y.mean()*X.dot(X)-X.mean()*Y.dot(X))/denominator

Y_hat = X*a + b
error = 1 - (Y-Y_hat).dot(Y-Y_hat)/(Y-Y.mean()).dot(Y-Y.mean())
print(error)

