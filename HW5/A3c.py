#!/usr/bin/env python
import string
import numpy as np
from math import *
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt
from numpy.linalg import inv

x = np.linspace(-10,10,10000,endpoint=True)

a= np.log(np.cosh(x))
b= np.log(cosh(2))+(np.tanh(2)*(x-2))+(0.5*((x-2)*(x-2)))
c= np.log(cosh(-3))+(np.tanh(-3)*(x+3))+(0.5*np.power((x+3),2))
plt.plot(x,a, label="f(x)")
plt.plot(x,b, label="Q(x,2)")
plt.plot(x,c, label="Q(x,-3)")
plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
plt.show()