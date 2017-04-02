#!/usr/bin/python

import sys
#we dont bother about mapper because order doesn't matter.
#so I used cat as mapper
num_words = 0
num_lines = 0

for line in sys.stdin:          # For every line in the input from stdin
    # we don't need value, but I am not sure what will be taken for key if there is no explicit splitter
    num_lines += 1
    num_words += len(line.split())

print("{0} {1}".format(num_lines, num_words))