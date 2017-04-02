#!/usr/bin/python
import sys

#the final number of potential popular urls will be equal to the number of reducer
#so I finnally get most one url via awk script

best = [None, 0]
current = [None, 0]

for line in sys.stdin:
    url, count = line.split('\t')
    count = int(count)
    if current[0] != url:
        best = max([best, current], key=lambda x:x[1])
        current = [url, count]
    else:
        current[1] += count
#don't forget the last entry
best = max([best, current], key=lambda x:x[1])
print "{}\t{}".format(best[0], best[1])
