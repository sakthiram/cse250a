#!/usr/bin/env python
import string
from collections import namedtuple
from operator import itemgetter

#Normalizing
def update_prob(table, index):
    global total_prob
    for i in range(len(table)):
       table[i][index] = float(table[i][index]/total_prob)
    return table

########################################
# STEP1: Import WCs & Init probability #
########################################

def init_WCP():
	#Named Tuple
	#wordTable = namedtuple('WordTable', 'word, count, probability, p_given_E')
	
	global WCP, total_prob
	WCP = []
	total_prob = 0.0
	
	import csv
	csv.register_dialect('space_delimiter', delimiter=' ')
	#for line in csv.reader(open("WCs/test.txt", "rb"), 'space_delimiter'):
	for line in csv.reader(open("WCs/hw1_word_counts_05.txt", "rb"), 'space_delimiter'):
	    line = [line[0], int(line[1]), int(line[1]), int(line[1])] 
	    #wordTable._make(line)
	    WCP.append(line)
	    total_prob += line[1]
	
	WCP = update_prob(WCP, 2)
	WCP = update_prob(WCP, 3)
	print "10 High Prob Words"
	print sorted(WCP, key=itemgetter(2), reverse=True)[:10]
	print "10 Low Prob Words"
	print sorted(WCP, key=itemgetter(2), reverse=False)[:10]

########################################
# STEP2: Form Letter-Probability table #
########################################

def init_LCP():

	global LCP, total_prob
	LCP = []
	total_prob = 0.0
	
	for letter in list(string.ascii_uppercase):
		lc = 0
		for wcp in WCP:
			lc += wcp[0].count(letter)*wcp[1];
	        total_prob += lc
		lcp = [letter, lc, lc, lc]
		LCP.append(lcp)
	
	LCP = update_prob(LCP, 2)
	LCP = update_prob(LCP, 3)


########################################
# STEP3: Find Best Guess from LP table #
########################################

def guess_next_letter():
	print "High Prob Letter"
	print sorted(LCP, key=itemgetter(3), reverse=True)[0]

####################################
# STEP4: Update Prob given Guesses #
####################################

def update_prob_given_evidence(correct_guesses, incorrect_guesses):

	global WCP, LCP, total_prob

	#Posterior Probability

	total_prob = 0.0

	for wcp in WCP:
		p_E = 1.0
		for guess in correct_guesses:	
			guessed_letter = guess[0]
			guessed_loc = guess[1]
			for letter_index in range(len(wcp[0])):
				if letter_index == guessed_loc and wcp[0][letter_index] != guessed_letter:
					p_E = 0.0
				#TODO
				if letter_index != guessed_loc and wcp[0][letter_index] == guessed_letter:
					p_E = 0.0

		for guess in incorrect_guesses:
			for wcp_letter in wcp[0]:
				if wcp_letter == guess:
					p_E = 0.0
		
		# Prob of W given E 
		wcp[3] = wcp[2]*p_E
		total_prob += wcp[3]

	WCP = update_prob(WCP, 3)


	#Predictive Probability

	total_prob = 0.0

	for lcp in LCP:	
		lcp[3] = 0.0

		letter_not_yet_guessed = 1.0
		#Already Guessed
		for guess in correct_guesses:	
			if lcp[0] == guess[0]:
				letter_not_yet_guessed = 0.0
		for guess in incorrect_guesses:
			if guess == lcp[0]:
				letter_not_yet_guessed = 0.0

		#Conditional Prob based on wcp[3]
		for wcp in WCP:
			letter_exists = 0.0
			for wcp_letter in wcp[0]:
				if lcp[0] == wcp_letter:
					letter_exists = 1.0
					#letter_exists += 1.0
			lcp[3] += letter_not_yet_guessed*letter_exists*wcp[3]

		total_prob += lcp[3]

	#LCP = update_prob(LCP, 3)

#################
# MAIN Function #
#################

if __name__ == "__main__":

	init_WCP()
	init_LCP()
	correct_guesses = [['A',0],['S',4]]
	incorrect_guesses = ['I']
	update_prob_given_evidence(correct_guesses, incorrect_guesses)
	guess_next_letter()	
