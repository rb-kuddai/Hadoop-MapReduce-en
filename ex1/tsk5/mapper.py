#!/usr/bin/python

import sys

#thanks to Rafal Dowgrid from http://stackoverflow.com/questions/5434891/iterate-a-list-as-pair-current-next-in-python
#I know - I just could remember previous result and iterate but I wanted something neater
import itertools
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)

for line in sys.stdin:
    words = line.split()
    for word1, word2 in pairwise(words):
        print("{0} {1}\t{2}".format(word1, word2, 1))