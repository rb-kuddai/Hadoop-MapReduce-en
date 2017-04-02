#!/usr/bin/python
import sys

#number of the most frequent words to track.
N_freq_words = 20
num_printed_words = 0

#it is meant to receive output of task 4 as its input
#and it should be sorted in the descending order
for line in sys.stdin:          # For ever line in the input from stdin
    if num_printed_words < N_freq_words:
        num_printed_words += 1
        print line.strip()


