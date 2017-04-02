#!/usr/bin/python
import sys
from collections import Counter

#have to create reducer in order to outprint 0.0 for electronic
target_d = "d1.txt"
counter = Counter()

for line in sys.stdin:
    #each term is unique as we are using output from task 1
    term, tf_idf = line.split("\t")
    term, tf_idf = term.strip(), float(tf_idf)
    counter[term] = tf_idf

#It is said that terms.txt is small enough to be held in memory (only 7 terms)
#For the same reason I am using only 1 reducer, as it will receive only 7 lines
for t in file('terms.txt'):
    t = t.strip()
    tf_idf = float(counter[t])
    print "{}, {} = {}".format(t, target_d, tf_idf)

