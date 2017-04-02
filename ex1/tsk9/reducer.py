#!/usr/bin/python
import sys
lowest_avg_score = None
eps = 0.000001

# from http://stackoverflow.com/questions/4028889/floating-point-equality-in-python
def approx_equal(a, b):
     return abs(a - b) < eps

for line in sys.stdin: # For every line in the input from stdin
    raw_avg_score, name = line.split("\t", 1)
    avg_score = float(raw_avg_score)

    if lowest_avg_score is None:
		lowest_avg_score = avg_score

    if approx_equal(avg_score, lowest_avg_score):
        print "{0} with {1}".format(name.strip(), avg_score)

