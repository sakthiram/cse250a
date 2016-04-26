#!/usr/bin/env python
import string
from collections import namedtuple
from operator import itemgetter

# with open("unigram.txt") as f:
#     unigram_content = f.readlines()
voc_lines = [line.rstrip('\n') for line in open('vocab.txt')]
uni_lines = [line.rstrip('\n') for line in open('unigram.txt')]

count = 0
total_count = 0
for idx in range(len(voc_lines)):
# 	if voc_lines[idx][0] == B:
# 		count_B += uni_lines[idx]
 	total_count += float(uni_lines[idx])

for idx in range(len(voc_lines)):
	if voc_lines[idx][0] == 'B':
		pB = float(float(uni_lines[idx])/total_count)
		print voc_lines[idx], "		", pB