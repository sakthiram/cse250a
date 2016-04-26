#!/usr/bin/env python
from math import *
import random as random
import numpy as np
import matplotlib.pyplot as plt

class likelihood_weighting:
	def __init__(self, *args):
		pB = 0.5
		n = 10
		err = 0.25
		z = 128.0

		num_samples = 1000000

		b = [0 for x in range(n)]
		p_b_given_z = []
		num = 0.0
		den = 0.0

		while(num_samples!=0):
			ind_b8 = 0
			for i in range(n):
				b[i] = np.random.randint(0,2)
				if (i == 7 and b[i] == 1):
					ind_b8 = 1
			
			fB = sum([pow(2,x)*b[x] for x in range(n)])
			# print "fB: ", fB

			p_z_given_Bs = ((1-err)/(1+err))*pow(err,abs(z-fB))
			# print "p_z_given_Bs: ", p_z_given_Bs
			num += ind_b8*p_z_given_Bs
			den += p_z_given_Bs
			print "num: ", num
			print "den: ", den
			if den == 0:
				continue
			else:
				p_b_given_z.append(num/den)
			
			print "p_b_given_z: ", (num/den)
			num_samples -= 1

		plt.plot(p_b_given_z)
		plt.ylabel('p_b_given_z')
		plt.show()




if __name__ == '__main__':
	lw = likelihood_weighting()