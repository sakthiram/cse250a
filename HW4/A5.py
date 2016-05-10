#!/usr/bin/env python
import string
import numpy as np
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt
from numpy.linalg import inv

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
a = 1
logging.debug('This message should go to the log file %d', a)
logging.debug('123')

# Extract xt into array
xt = np.array([])
file_2000 = open("nasdaq00.txt", "r")
for line in file_2000:
    xt=np.append(xt,float(line.rstrip()))

#print xt

# Calculate A max
A = np.zeros(shape=(4,4))
for t in range(4,len(xt)):
	x = np.array([[xt[t-1]], [xt[t-2]], [xt[t-3]], [xt[t-4]]])
	#print x
	A += np.mat(x)*(np.mat(x.transpose()))

#print A

# Calculate A inverse
A_inv = inv(A)

# Calculate b vector
b = np.zeros(shape=(4,1))
for t in range(4,len(xt)):
	x = [[xt[t-1]], [xt[t-2]], [xt[t-3]], [xt[t-4]]]
	b += xt[t]*np.mat(x)

# Calculate weight vector
w = np.mat(A_inv)*np.mat(b)
print w

# MSE
sum_of_sq = 0.0
for t in range(4,len(xt)):
	sum_of_sq += (xt[t] - (w[0]*xt[t-1] + w[1]*xt[t-2] + w[2]*xt[t-3] + w[3]*xt[t-4]))**2

mse = sum_of_sq/(len(xt)-4)
print mse

# Extract xt into array
lxt = len(xt)
xt = np.array([xt[lxt-4], xt[lxt-3], xt[lxt-2],xt[lxt-1]])
file_2001 = open("nasdaq01.txt", "r")
for line in file_2001:
    xt=np.append(xt,float(line.rstrip()))

# MSE
sum_of_sq = 0.0
for t in range(4,len(xt)):
	sum_of_sq += (xt[t] - (w[0]*xt[t-1] + w[1]*xt[t-2] + w[2]*xt[t-3] + w[3]*xt[t-4]))**2

mse = sum_of_sq/(len(xt)-4)
print mse


