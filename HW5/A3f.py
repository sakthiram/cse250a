#!/usr/bin/env python
import string
import numpy as np
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt
from numpy.linalg import inv

x = []
x0 = -3
for i in range(10):
	if i == 0:
		x.append(x0)
	else :
		x.append(x[i-1] - np.tanh(x[i-1]))


plt.plot(x)
plt.ylabel('x(n)')
plt.show()
