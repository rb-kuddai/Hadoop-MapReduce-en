#!/usr/bin/python

import sys
#we dont bother about mapper because order doesn't matter.as
#so I used ca
total_num_words = 0
total_num_lines = 0

for line in sys.stdin:          # For ever line in the input from stdin
    num_lines, num_words = line.split()
    total_num_lines += int(num_lines)
    total_num_words += int(num_words)

print("{0} {1}".format(total_num_lines, total_num_words))