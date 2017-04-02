#!/usr/bin/python
import sys
import re
from math import log10

#it is said that it is fine to hard-code  total number of documents in one place
#"""For tf-idf, you can hard-code N. But please hard-code it in only one place."""
total_num_docs = 17.0
target_d = "d1.txt"
terms = set()

#It is said that terms.txt is small enough to be held in memory (only 7 terms)
#For the same reason I am using only 1 reducer, as it will receive only 7 lines
for t in file('terms.txt'):
    terms.add(t.strip())
#as we are using input from task
#each term in the inverted index must be unique

for line in sys.stdin:
    #print line
    t, num_docs, freqs_str = re.split(r"\s+:\s+", line)
    t, num_docs, freqs_str = t.strip(), int(num_docs), freqs_str.strip()

    if t not in terms:
        continue

    freqs = re.findall(r"\(([\w\d\.]+?),\s*(\d+)\)", freqs_str)
    tf = next((float(f) for d, f in freqs if d == target_d), 0.0)
    idf = log10(total_num_docs / (1.0 + num_docs))
    print '{0}\t{1}'.format(t, tf * idf)
