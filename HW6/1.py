#!/usr/bin/env python
import string
import numpy as np
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt
from numpy.linalg import inv
import csv

# n = 23
# T = 267
# X = np.zeros(shape=(T,n)) 
# t = 0

m = 2
n = 26

# Observations (O1, O2, ... OT)
# O = np.array([])
# import csv
# csv.register_dialect('space_delimiter', delimiter=' ')
# for line in csv.reader(open("observations.txt", "rb"), 'space_delimiter'):
# 	for obs in range(len(line)):
# 		O = np.append(O, int(line[obs]))
# np.save('observations.npy', O)

O = np.load('observations.npy')

T = len(O)

# Init state Prob
I = np.array([])
file = open("initialStateDistribution.txt", "r")
for line in file:
	I = np.append(I,float(line.rstrip()))
file.close()

# Transition Matrix
A = np.array([])
first = 1
csv.register_dialect('space_delimiter', delimiter=' ')
for line in csv.reader(open("transitionMatrix.txt", "rb"), 'space_delimiter'):
	tmp = np.array([])
	for j in range(len(line)-1): # Last char is \n
		tmp = np.append(tmp, float(line[j]))
	
	if first == 1:
		A = np.append(A, np.log(tmp))
		first = 0
	else:
		A = np.vstack((A, np.log(tmp)))

# Emission Matrix
B = np.array([])
first = 1
csv.register_dialect('space_delimiter', delimiter='	')
for line in csv.reader(open("emissionMatrix.txt", "rb"), 'space_delimiter'):
	tmp = np.array([])
	for k in range(len(line)):
		tmp = np.append(tmp, float(line[k]))
	
	if first == 1:
		B = np.append(B, np.log(tmp))
		first = 0
	else:
		B = np.vstack((B, np.log(tmp)))

l = np.array([])
# STEP1: Max Log Likelihood (Base Case)
tmp = np.array([])
for i in range(n):
	obs = O[0]
	tmp = np.append(tmp, np.log(I[i])+B[i][obs])
l = tmp.reshape(n,1)
print "Step 1 Done"


# STEP2: Max Log Likelihood (Recursion)
for t in range(1, T):
	obs = O[t]
	tmp = np.array([])
	for j in range(n):
		# max_likelihood_j = l[0][t-1] + A[0][j] + B[j][obs]
		# max_likelihood_j = l[(t-1)*n+0] + A[0][j] 
		lij = np.array([])
		for i in range(n):
			# lij = l[(t-1)*n+i] + A[i][j]
			lij = np.append(lij, l[i][t-1] + A[i][j] + B[j][obs])
			# if (lij > max_likelihood_j):
			# 	max_likelihood_j = lij
		# l = np.append(l, max_likelihood_j+ B[j][obs])
		# tmp = np.append(tmp, max_likelihood_j)
		tmp = np.append(tmp, np.amax(lij))
	l = np.vstack((np.transpose(l),tmp)).T
print "Step 2 Done"
np.save('lMatrix.npy', l)


S_flipped = np.array([])
# STEP3: Back Tracking (Base Case)
S_flipped = np.append(S_flipped, np.argmax(l[:,T-1]))
print S_flipped

# STEP4: Back Tracking (Recursion)
for t in range(T-2, -1, -1):
	obs = O[t]
	likelihood_j = np.array([])
	j = S_flipped[(T-1)-(t+1)]
	for i in range(n):
		# likelihood_j = np.append(likelihood_j, l[i+(t+1)*n] + A[i][j] + B[j][obs])
		likelihood_j = np.append(likelihood_j, l[i][t+1] + A[i][j] + B[j][obs])
	S_flipped = np.append(S_flipped, np.argmax(likelihood_j))

S = S_flipped[::-1]
np.save('sMatrix.npy', S)

print "Plotting"
plt.xticks(np.arange(0,150000,50000))
plt.yticks(range(26), string.lowercase)
plt.plot(S)
plt.grid()
#plt.legend()
plt.show()