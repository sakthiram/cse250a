#!/usr/bin/env python
import string
import numpy as np
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt
from numpy.linalg import inv


# Extract xt into array
xt = np.array([])
file_2000 = open("nasdaq00.txt", "rb")
for line in file_2000:
    np.append(xt,line)

# Calculate A max
A = np.zeros(shape=(4,4))
for t from 5 to range(len(xp)):
	x = [[xt[t-1]], [xt[t-2]], [xt[t-3]], [xt[t-4]]]
	A += np.mat(x)*np.mat(x.transpose())

# Calculate A inverse
A_inv = inv(A)

# Calculate b vector
b = np.zeros(shape=(4,1))
for t from 5 to range(len(xp)):
	x = [[xt[t-1]], [xt[t-2]], [xt[t-3]], [xt[t-4]]]
	b += xt[t]*np.mat(x)

# Calculate weight vector
w = np.mat(A_inv)*np.mat(b)
print w