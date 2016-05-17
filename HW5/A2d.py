#!/usr/bin/env python
import string
import numpy as np
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt
from numpy.linalg import inv

n = 23
T = 267
X = np.zeros(shape=(T,n)) 
t = 0

import csv
csv.register_dialect('space_delimiter', delimiter=' ')
for line in csv.reader(open("spectX.txt", "rb"), 'space_delimiter'):
	for i in range(n):
		X[t][i] = int(line[i])
	t += 1

Y = np.array([])
file_Y = open("spectY.txt", "r")
for line in file_Y:
	Y = np.append(Y,float(line.rstrip()))

p = [2.0/n] *n

print p

for iteration in range(257):
	if iteration>0:
		den = np.array([])
		for t in range(T):
			noisyOrProd = 1
			for i in range(n):
				noisyOrProd *= np.power((1-p[i]),X[t][i])
			denominator = 1 - noisyOrProd
			den = np.append(den,denominator) 

		#Update p
		for i in range(n):
			pNew = 0.0
			Ti = 0
			for t in range(T):
				pNew += Y[t]*X[t][i]*p[i]/den[t]
				Ti += int(X[t][i] == 1)
			p[i] = pNew/Ti

	#Calculate Mistakes & Log likelihood
	M = 0
	L = 0
	for t in range(T):
		noisyOrProd = 1
		for i in range(n):
			noisyOrProd *= np.power((1-p[i]),X[t][i])
		pY = 1 - noisyOrProd
		if ((Y[t] == 0 and pY >= 0.5) or (Y[t] == 1 and pY <= 0.5)):
			M += 1
		if (Y[t] == 0):
			pY = noisyOrProd
		L += np.log(pY)
	L = L/T

	print "iter: ", iteration, "   M: ", M, "   L: ", L 

