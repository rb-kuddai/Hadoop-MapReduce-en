#!/usr/bin/python
import sys

best = [None, 0]
current = [None, 0]

for line in sys.stdin:
    owner_id, count = line.split('\t')
    count = int(count)
    if current[0] != owner_id:
        best = max([best, current], key=lambda x:x[1])
        current = [owner_id, count]
    else:
        current[1] += count
#don't forget the last entry
best = max([best, current], key=lambda x:x[1])
print "{}\t{}".format(best[0], best[1])
