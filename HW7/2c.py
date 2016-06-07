#!/usr/bin/env python
import string
from collections import namedtuple
from operator import itemgetter
import csv
import random as r
import numpy as np
from numpy.linalg import inv

prob_a1 = [[] for _ in range(82)] # Start from 1-81 (0 not used)
csv.register_dialect('space_delimiter', delimiter=' ')
for line in csv.reader(open("prob_a1.txt", "rb"), 'space_delimiter'):
    newState_Prob = [int(line[2]), float(line[4])] 
    prob_a1[int(line[0])].append(newState_Prob)

prob_a2 = [[] for _ in range(82)] # Start from 1-81 (0 not used)
csv.register_dialect('space_delimiter', delimiter=' ')
for line in csv.reader(open("prob_a2.txt", "rb"), 'space_delimiter'):
    newState_Prob = [int(line[2]), float(line[4])] 
    prob_a2[int(line[0])].append(newState_Prob)

prob_a3 = [[] for _ in range(82)] # Start from 1-81 (0 not used)
csv.register_dialect('space_delimiter', delimiter=' ')
for line in csv.reader(open("prob_a3.txt", "rb"), 'space_delimiter'):
    newState_Prob = [int(line[2]), float(line[4])] 
    prob_a3[int(line[0])].append(newState_Prob)

prob_a4 = [[] for _ in range(82)] # Start from 1-81 (0 not used)
csv.register_dialect('space_delimiter', delimiter=' ')
for line in csv.reader(open("prob_a4.txt", "rb"), 'space_delimiter'):
    newState_Prob = [int(line[2]), float(line[4])] 
    prob_a4[int(line[0])].append(newState_Prob)

prob_actions = []
prob_actions.append(prob_a1)
prob_actions.append(prob_a2)
prob_actions.append(prob_a3)
prob_actions.append(prob_a4)

P = [] # P[action][cur_state][next_state]-- Fill in 0s
for a in range(len(prob_actions)):
	prob_listOflist = []
	for s in range(0,82):
		prob_list = []
		for next_state in range(0,82):
			prob = 0
			for check_state in prob_actions[a][s]:
				if next_state == check_state[0]:
					prob = check_state[1]
			prob_list.append(prob)				 
		prob_listOflist.append(prob_list)
	P.append(prob_listOflist)

discount = 0.9875

rewards = [0.0] # start ith so that you start appending from 1-81
file = open("rewards.txt", "r")
for line in file:
    rewards.append(float(line.rstrip()))

R_mat = np.matrix(rewards)
I_mat = np.identity(82)

numbered_cells = [3,11,12,15,16,17,20,22,23,24,26,29,30,31,34,35,39,43,48,52,53,56,57,58,59,60,61,62,66,70,71]
numbered_cells_PIs = ['WEST' for _ in range(len(numbered_cells))]

directions = ['WEST', 'NORTH', 'EAST', 'SOUTH']
PI_index = [r.choice(range(4)) for _ in range(82)]
temp_PI_index = [0 for _ in range(82)]
PI = [directions[i] for i in PI_index]

iteration = 0
while True:

	# Policy Evaluation <Given PI_index> 
	prob_given_PI = []
	for s,action in enumerate(PI_index):
		prob_given_PI.append(P[action][s])
	#print prob_given_PI
	P_mat = np.mat(prob_given_PI)

	x = inv(np.mat(I_mat) - discount*np.mat(P_mat))
	V = np.mat(x)*np.transpose(R_mat)

	# Policy Improvement
	for s in range(1,82):
		max_value = float('-inf')
		arg_max = 0

		for a in range(len(prob_actions)):
			v_action = 0.0
			for possible_state in prob_actions[a][s]:
				s_next = possible_state[0]
				p_next = possible_state[1]
			 	v_action += p_next*V[s_next]
				#print v_action
			if (v_action > max_value):
				max_value = v_action
				arg_max = a
		PI[s] = directions[arg_max]
		temp_PI_index[s] = arg_max

	for i,cell in enumerate(numbered_cells):
		numbered_cells_PIs[i] = PI[cell]

	iteration += 1
	if (PI_index == temp_PI_index):
		print iteration
		#print V
		print numbered_cells_PIs
		break

	for s in range(1,82):
		PI_index[s] = temp_PI_index[s]

