#!/usr/bin/python

import sys
import json
from collections import Counter

#There is no point of using sys.stdout.write because
#on the reducer side we have to count number of documents where each term occurs
#AND OUTPUT IT RIGHT AFTER THE TERM.
#The would be sence to use sys.stdout.write if the format was like this:
#cat : {(d1.txt, 2), (d2.txt, 3)} : 2
#instead of this:
#cat : 2 : {(d1.txt, 2), (d2.txt, 3)}
#THERE IS ONLY 17 FILES so we can store 17 counts in RAM easily
#And I use second map reduce job to sort it alphabetically by term, so
#at some point entire string will be stored in RAM.

#The Bottleneck of the performance will be the number of documents
#(not size of the documents). but taking into consideration that
# the HADOOP block size (128mb or 64mb) we will have to
#combine many small documents into on several corpuses.

current_term = None
current_term_counter = Counter()

def print_current():
    if len(current_term_counter) > 0:
        #ensure alphabetical sorting by file name.
        #From the task description:
        #"""
        #and also that the items inside lists are also
        #sorted alphabetically by document identifier
        #"""
        #So sort file_names as strings like:
        #horse	: 11 : {(d1.txt, 17), (d10.txt, 10), (d12.txt, 2), (d13.txt, 6), (d15.txt, 3), (d2.txt, 7), (d4.txt, 1), (d5.txt, 1), (d6.txt, 5), (d7.txt, 14), (d9.txt, 75)}
        frequencies = sorted(current_term_counter.iteritems(), key=lambda f: f[0])
        #formating as in task
        frequencies_str = ', '.join(['({}, {})'.format(*f) for f in frequencies])
        num_docs = len(current_term_counter)
        print "{0} : {1} : {{{2}}}".format(current_term, num_docs, frequencies_str)

for line in sys.stdin:
    #freqs_json -> frequencies like  {"d1.txt": 5, "d2.txt": 8}
    term, freqs_json = line.split("\t", 1)
    #assume that we have only ascii anyway
    #so u'cat' == 'cat'
    counter = Counter(json.loads(freqs_json))

    if term != current_term:
        print_current()
        #clear everything for the next term
        current_term = term.strip()
        current_term_counter.clear()

    current_term_counter += counter

#print the last term
print_current()
