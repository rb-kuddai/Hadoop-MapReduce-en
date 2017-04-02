#!/usr/bin/python
import sys
import re

for line in sys.stdin:
    match = re.search(r'".*?\s+(.+?)(?:\s+.+?"|")', line)
    #there are broken lines like this one
    #k7us70a.krhm.jvc-victor.co.jp - - [06/Aug/1995
    #so taking counter measures
    if match:
        url = match.group(1)
        print "{}\t{}".format(url, 1)

