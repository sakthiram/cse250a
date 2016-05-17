#!/usr/bin/env python
import string
import numpy as np
from math import *
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt
from numpy.linalg import inv

x = np.linspace(-4,4,10000,endpoint=True)
g = 0.0
for i in range(1,11):
	g += np.log(np.cosh(x+(1/np.sqrt((i*i)+1))))
g = g/10.0

a= np.log(np.cosh(x))
plt.plot(x,a, label="g(x)")
plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
plt.show()