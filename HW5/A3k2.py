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
		xnew = 0.0
		for j in range(1,11):
			xnew += np.tanh(x[i-1]+(1/np.sqrt(j*j+1)))
		x.append(x[i-1] - xnew/10)

#Final value
g = 0.0
for j in range(1,11):
	g += np.log(np.cosh((x[9]+(1/np.sqrt(j*j+1)))))
gMin = g/10

print "gMin: ", gMin, "   x: ", x[9] 

plt.plot(x)
plt.ylabel('x(n)')
plt.show()
