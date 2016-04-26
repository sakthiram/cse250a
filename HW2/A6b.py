#!/usr/bin/env python
import string
from collections import namedtuple
from operator import itemgetter

# with open("unigram.txt") as f:
#     unigram_content = f.readlines()
voc_lines = [line.rstrip('\n') for line in open('vocab.txt')]

bi_lines = []

import csv
csv.register_dialect('space_delimiter', delimiter='	')
for line in csv.reader(open("bigram.txt", "rb"), 'space_delimiter'):
    line = [int(line[0]), int(line[1]), int(line[2])] 
    bi_lines.append(line)
	
given_word = 'ONE'
given_word_idx = voc_lines.index('ONE')

count = 0
total_count = 0

for idx in range(len(bi_lines)):
	total_count += bi_lines[idx][2]

bigram_prob_list = []
for idx in range(len(bi_lines)):
	if bi_lines[idx][0] == given_word_idx+1:
		pB = float(float(bi_lines[idx][2])/total_count)
		index = bi_lines[idx][1]-1
		bigram_prob_list.append([voc_lines[index],pB])

print sorted(bigram_prob_list, key=itemgetter(1), reverse=True)[:10]

