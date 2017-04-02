#!/usr/bin/python
import sys
import heapq
from operator import itemgetter

#using heap to collect top ones
N = 10
top_hosts = [(0, None)] * N
heapq.heapify(top_hosts)

current_count = 0
current_host = None

for line in sys.stdin:
    host, count = line.split('\t')
    count = int(count)
    if current_host != host:
        heapq.heappushpop(top_hosts, (current_count, current_host))
        current_host = host
        current_count = count
    else:
        current_count += count
#don't forget the last entry
heapq.heappushpop(top_hosts, (current_count, current_host))
#clean from initial None entries if any of them are left
top_hosts = filter(lambda x: x[1] is not None, top_hosts)
top_hosts = sorted(top_hosts, key=itemgetter(0), reverse=True)
for count, host in top_hosts:
    print "{}\t{}".format(host, count)