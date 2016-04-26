#!/usr/bin/env python
import string
import numpy as np
from collections import namedtuple
from operator import itemgetter
import matplotlib.pyplot as plt


def get_Lu(sentence):
	final_prob = 1
	for i in range(len(sentence)):
		for idx in range(len(voc_lines)):
			if voc_lines[idx] == sentence[i].upper():
				prob = float(float(uni_lines[idx])/total_uni_count)
		final_prob *= prob
	return np.log(final_prob)

def get_Lb(sentence):
	final_prob = 1
	for i in range(len(sentence)):
		prob = 0
		if  i == 0:
			given_word_idx = voc_lines.index('<s>')
			current_word_idx = voc_lines.index(sentence[i].upper())
			for idx in range(len(voc_lines)):
				if voc_lines[idx] == sentence[i].upper():
					prob = float(float(uni_lines[idx])/total_uni_count)
					break
		else:
			given_word_idx = voc_lines.index(sentence[i-1].upper())
			current_word_idx = voc_lines.index(sentence[i].upper())

		for idx in range(len(bi_lines)):
			if bi_lines[idx][0] == given_word_idx+1 and bi_lines[idx][1] == current_word_idx+1:
				prob = float(float(bi_lines[idx][2])/get_total_bi_count(bi_lines[idx][0]))
		final_prob *= prob
	return np.log(final_prob)

def get_Lm(sentence, lambda_val):
	final_prob = 1
	for i in range(len(sentence)):
		prob_b = 0
		if  i == 0:
			given_word_idx = voc_lines.index('<s>')
			current_word_idx = voc_lines.index(sentence[i].upper())
			for idx in range(len(voc_lines)):
				if voc_lines[idx] == sentence[i].upper():
					prob_b = float(float(uni_lines[idx])/total_uni_count)
					break
		else:
			given_word_idx = voc_lines.index(sentence[i-1].upper())
			current_word_idx = voc_lines.index(sentence[i].upper())

		for idx in range(len(bi_lines)):
			if bi_lines[idx][0] == given_word_idx+1 and bi_lines[idx][1] == current_word_idx+1:
				prob_b = float(float(bi_lines[idx][2])/get_total_bi_count(bi_lines[idx][0]))

		for idx in range(len(voc_lines)):
			if voc_lines[idx] == sentence[i].upper():
				prob_u = float(float(uni_lines[idx])/total_uni_count)

		final_prob *= (1-lambda_val)*prob_u + lambda_val*prob_b
	return np.log(final_prob)



def get_total_bi_count(prev_word_idx):
	total_count = 0
	for idx in range(len(bi_lines)):
		if bi_lines[idx][0] == prev_word_idx:
			total_count += bi_lines[idx][2]
	return total_count


def total_count_uni():
	total_count = 0
	for idx in range(len(voc_lines)):
	 	total_count += float(uni_lines[idx])
	return total_count

def total_count_bi():
	total_count = 0
	for idx in range(len(bi_lines)):
		total_count += bi_lines[idx][2]
	return total_count

def uni_prob(start_letter):
	with open('6a.txt', 'w') as file:
		for idx in range(len(voc_lines)):
			if voc_lines[idx][0] == start_letter:
				pB = float(float(uni_lines[idx])/total_uni_count)
				#print voc_lines[idx], "		", pB
				file.write(voc_lines[idx] + '	' + str(pB) + '\n')

def bi_prob(given_word):
	given_word_idx = voc_lines.index('ONE')
	bigram_prob_list = []
	for idx in range(len(bi_lines)):
		if bi_lines[idx][0] == given_word_idx+1:
			pB = float(float(bi_lines[idx][2])/get_total_bi_count(given_word_idx+1))
			index = bi_lines[idx][1]-1
			bigram_prob_list.append([voc_lines[index],pB])
	with open('6b.txt', 'w') as file:
		sorted_list = sorted(bigram_prob_list, key=itemgetter(1), reverse=True)[:10]
		file.write(str(sorted_list))


# Get lines
voc_lines = [line.rstrip('\n') for line in open('vocab.txt')]
uni_lines = [line.rstrip('\n') for line in open('unigram.txt')]

bi_lines = []

import csv
csv.register_dialect('space_delimiter', delimiter='	')
for line in csv.reader(open("bigram.txt", "rb"), 'space_delimiter'):
    line = [int(line[0]), int(line[1]), int(line[2])] 
    bi_lines.append(line)

count = 0
total_uni_count = total_count_uni()
total_bi_count = total_count_bi()

#####
#6a.#
#####
#Uniprob for 'B'
uni_prob('B')
bi_prob('ONE')

# Unigram Log
sentence = ["The","stock","market","fell","by","one","hundred","points","last","week"]
Lu = get_Lu(sentence)
print Lu
Lb = get_Lb(sentence)
print Lb

sentence2 = ["The","fourteen","officials","sold","fire","insurance"]
Lu = get_Lu(sentence2)
print Lu
Lb = get_Lb(sentence2)
print Lb

Lm_list = []
for i in range(100):
	Lm = get_Lm(sentence2, float(i/100.0))
	Lm_list.append(Lm)

plt.plot(Lm_list)
plt.ylabel('Lm_list')
plt.show()



