# -*- coding: utf-8 -*-
"""Perceptron prosty 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tZGyYB6pPXVkpICDi5HQtaNxDf9xtSQz
"""

import numpy as np
import tqdm

def hardlims(input):
  return (input >0 ).astype(float)

def delta_rule(X,Y, weights,n_epochs):
  dims = X.shape[-1]
  for _ in tqdm.tqdm(range(n_epochs)):
    for x,y in zip(X,Y):
      sum = x@weights
      e = y - hardlims(sum)
      # print(e*x)
      weights = weights + e*x
      # print("w", weights, "k")
  return weights

"""#AND"""

#AND
X = np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
Y = np.array([0,0,0,1])

weights = np.random.random(size=(X.shape[-1]))
print(weights)
print(X@weights)
print(hardlims(X@weights))
print("")

weights = delta_rule(X,Y, weights,n_epochs=100000)

print("Wagi")
print(X@weights)
print(hardlims(X@weights))
Y

"""#OR"""

#OR
X = np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
Y = np.array([0,1,1,1])

weights = np.random.random(size=(X.shape[-1]))
print(weights)
print(X@weights)
print(hardlims(X@weights))
print("")

weights = delta_rule(X,Y, weights,n_epochs=100000)

print("Wagi")
print(X@weights)
print(hardlims(X@weights))
Y

"""#XOR"""

#XOR
X = np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
Y = np.array([0,1,1,0])

weights = np.random.random(size=(X.shape[-1]))
print(weights)
print(X@weights)
print(hardlims(X@weights))
print("")

weights = delta_rule(X,Y, weights,n_epochs=100000)

print("Wagi")
print(X@weights)
print(hardlims(X@weights))
Y