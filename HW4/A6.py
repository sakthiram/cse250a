#!/usr/bin/env python
import string
import numpy as np
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt
from numpy.linalg import inv

# Extract images into array
x0 = np.zeros(shape=(700,64)) #3
x1 = np.zeros(shape=(700,64)) #5
y0 = np.zeros(shape=(700,1))  #3
y1 = np.ones(shape=(700,1))  #3

image = 0
import csv
csv.register_dialect('space_delimiter', delimiter=' ')
for line in csv.reader(open("newTrain3.txt", "rb"), 'space_delimiter'):
	for pixel in range(64):
   		x0[image][pixel] = int(line[pixel])
   	image += 1

image = 0
csv.register_dialect('space_delimiter', delimiter=' ')
for line in csv.reader(open("newTrain5.txt", "rb"), 'space_delimiter'):
	for pixel in range(64):
   		x1[image][pixel] = int(line[pixel])
   	image += 1

x = np.concatenate((x0,x1), axis=0)
y = np.concatenate((y0,y1), axis=0)
w = np.zeros(shape=(64,1))

L_list = []

# Iterate for many times to see a good value for likelihood
for i in range(10):
	d1 = np.zeros(shape=(1,64))
	d2 = np.zeros(shape=(64,64))

	dot_product = np.mat(x)*np.mat(w)
	L = 0.0
	for index in range(len(dot_product)):
		sigma = 1/(1+np.exp(-dot_product[index]))
		sigma_n = 1/(1+np.exp(dot_product[index]))
		d1 += (y[index]-sigma)*np.mat(x[index])
		temp = (np.mat(x[index].reshape(64,1))*np.mat(x[index]))
		d2 -= (np.asscalar(sigma*sigma_n))*np.mat(temp)
		L += y[index]*np.mat(np.log(sigma))+(1-y[index])*np.mat(np.log(sigma_n))

	L_list.append(np.asscalar(L))
	print "L: ", L
	d2_inv = inv(d2)

	w = w-np.mat(d2_inv)*np.mat(d1.T)
	error = 0.0
	for index in range(len(y)):
		p = 1/(1+np.exp(-np.mat(x[index])*np.mat(w)))
		#print "p = ", p
		if ((p <= 0.5 and y[index] != 0) or (p > 0.5 and y[index] != 1)):
			error += 1.0
	err_rate = float(error/len(y))
	print "Training Error Rate: ", err_rate

print w.reshape(8,8)

# Testing
x0 = np.zeros(shape=(400,64)) #3
x1 = np.zeros(shape=(400,64)) #5
y0 = np.zeros(shape=(400,1))  #3
y1 = np.ones(shape=(400,1))  #5

image = 0
import csv
csv.register_dialect('space_delimiter', delimiter=' ')
for line in csv.reader(open("newTest3.txt", "rb"), 'space_delimiter'):
	for pixel in range(64):
   		x0[image][pixel] = int(line[pixel])
   	image += 1

image = 0
csv.register_dialect('space_delimiter', delimiter=' ')
for line in csv.reader(open("newTest5.txt", "rb"), 'space_delimiter'):
	for pixel in range(64):
   		x1[image][pixel] = int(line[pixel])
   	image += 1

x = np.concatenate((x0,x1), axis=0)
y = np.concatenate((y0,y1), axis=0)

error = 0.0
for index in range(len(y)):
	p = 1/(1+np.exp(-np.mat(x[index])*np.mat(w)))
	#print "p = ", p
	if ((p <= 0.5 and y[index] != 0) or (p > 0.5 and y[index] != 1)):
		error += 1.0

err_rate = float(error/len(y))
print "Testing Error Rate: ", err_rate

plt.plot(L_list)
plt.ylabel('L_list')
plt.show()
