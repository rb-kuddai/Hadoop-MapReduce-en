#!/usr/bin/python
import sys
from datetime import datetime, timedelta

cur_host = None
cur_first_time = float('inf')
cur_last_time = -1
cur_unique = None

def print_time_mark():
    if cur_host is None:
        return
    if cur_unique == 1:
        #something like
        #1995-08-06 11:28:30
        #just time mark
        result = str(datetime.utcfromtimestamp(cur_first_time))
    else:
        #[days], hh:mm:ss
        result = "{:0>8}".format(timedelta(seconds=(cur_last_time - cur_first_time)))
    print "{}\t{}".format(cur_host, result)

#lines are sorted by host and seconds
for line in sys.stdin:
    line = line.strip()
    host, first_time, last_time, unique = line.split("\t")
    host = host.strip()
    first_time, last_time, unique = int(first_time), int(last_time), int(unique)

    if cur_host != host:
        print_time_mark()
        cur_host = host
        cur_first_time = first_time
        cur_last_time  = last_time
        cur_unique = unique
    else:
        cur_unique = 0

    cur_first_time = min(first_time, cur_first_time)
    cur_last_time  = max(last_time,  cur_last_time)

#don't forget the last entry
print_time_mark()