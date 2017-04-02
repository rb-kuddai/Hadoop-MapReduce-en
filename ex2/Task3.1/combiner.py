#!/usr/bin/python
import sys

#on combiner I am only counting instead of storing top 10 in the heap
#because the host_name is not unique in the log file. Therefore, the
#same host can appear in different mapper/combiner. Imagine situation
#where on each mapper you have a host which is only 21st on each particular
#mapper/combiner but if you assemble it from all the instances it may be potentially
#the first one!!

current_count = 0
current_url = None

def print_current():
    if current_url is not None:
        print "{}\t{}".format(current_url, current_count)

for line in sys.stdin:
    url, count = line.split('\t')
    count = int(count)
    if current_url != url:
        print_current()
        current_url = url
        current_count = count
    else:
        current_count += count
#don't forget the last entry
print_current()