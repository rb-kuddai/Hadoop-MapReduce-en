#!/usr/bin/python
import sys
import re
from datetime import datetime as dt

#Instead of secondary sorting I output
#host, first_time, last_time, is_unique
#which allows me to do kind of fast bubble sorting on
#first_time and last_tiem field via min and max.
#The advantage of this approach that it allows
#to use combiners, so you can produce only best
#approximation so far per one host via combiners.

#epoch: 1st January 1970
epoch = dt.utcfromtimestamp(0)

for line in sys.stdin:
    host, rest = line.split(" - - ")
    match = re.search(r'\[(.+?)\s+.+?]', rest)
    #there are broken lines like this one
    #k7us70a.krhm.jvc-victor.co.jp - - [06/Aug/1995
    #so taking counter measures
    if match:
        request_time = dt.strptime(match.group(1),'%d/%b/%Y:%H:%M:%S')
        seconds = (request_time - epoch).total_seconds()
        seconds = int(seconds)
        #is_inique to distinguish cases when person visited several URL
        #but at the same time, so it has 0 time difference. In contrast for
        #person who asked only for one URL we should output timestamp of the visit
        #(based on the prof. Kenneth answer that we should treat each entry to the server
        #as separate visit)
        #is_inique: 0 - False, 1 - True
        #host, first_time, last_time, is_unique
        print "{}\t{}\t{}\t{}".format(host.strip(), seconds, seconds, 1)