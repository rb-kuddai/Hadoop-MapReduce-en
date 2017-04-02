#!/usr/bin/python
import sys
import re

for line in sys.stdin:
    host, rest = line.split(" - - ")
    match = re.search(r'"\s+404\s+', rest)
    #there are broken lines like this one
    #k7us70a.krhm.jvc-victor.co.jp - - [06/Aug/1995
    #so taking counter measures
    if match:
        print "{}\t{}".format(host, 1)

