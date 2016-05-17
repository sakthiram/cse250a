#!/usr/bin/env python
import string
import numpy as np
from math import *
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt
from numpy.linalg import inv

x = np.linspace(-1.2,1.2,1000,endpoint=True)
#x = np.linspace(-0.2,0.2,100,endpoint=True)
func = (abs(x) - abs(x-(np.cosh(x)*np.sinh(x))))
print abs(x)
print abs(x-(np.cosh(x)*np.sinh(x)))
plt.plot(x, func)
plt.show()