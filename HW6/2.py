#!/usr/bin/env python
import string
import numpy as np
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt
from numpy.linalg import inv
import csv

S = np.load('sMatrix.npy')
print "Plotting"
plt.xticks(np.arange(0,150000,50000))
plt.yticks(range(26), string.lowercase)
plt.plot(S)
plt.grid()
#plt.legend()
plt.show()