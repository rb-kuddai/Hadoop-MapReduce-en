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

#I am using counter and json
#as I don't know whether I encounter reduce-side combiner or not
current_term = None
current_term_counter = Counter()

def print_current_counter():
    if len(current_term_counter) > 0:
        #produce something like:
        # {"d1.txt": 5, "d2.txt": 8}
        freqs_json = json.dumps(current_term_counter)
        print "{0}\t{1}".format(current_term, freqs_json)

for line in sys.stdin:
    #freqs_json -> frequencies like  {"d1.txt": 5, "d2.txt": 8}
    term, freqs_json = line.split("\t", 1)
    #assume that we have only ascii anyway
    #so u'cat' == 'cat'
    counter = Counter(json.loads(freqs_json))

    if term != current_term:
        print_current_counter()
        #clear everything for the next term
        current_term = term
        current_term_counter.clear()

    current_term_counter += counter

#print the last term
print_current_counter()
