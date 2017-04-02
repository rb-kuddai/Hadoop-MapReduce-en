#!/usr/bin/python
import sys
cur_host = None
cur_first_time = float('inf')
cur_last_time = -1
cur_unique = None

def print_first_last():
    if cur_host is not None:
        print "{}\t{}\t{}\t{}".format(cur_host, cur_first_time, cur_last_time, cur_unique)

#lines are sorted by host
for line in sys.stdin:
    line = line.strip()
    host, first_time, last_time, unique = line.split("\t")
    host = host.strip()
    first_time, last_time, unique = int(first_time), int(last_time), int(unique)

    if cur_host != host:
        print_first_last()
        cur_host = host
        cur_first_time = first_time
        cur_last_time  = last_time
        cur_unique =  unique
    else:
        cur_unique = 0


    cur_first_time = min(first_time, cur_first_time)
    cur_last_time  = max(last_time,  cur_last_time)

#don't forget the last entry
print_first_last()