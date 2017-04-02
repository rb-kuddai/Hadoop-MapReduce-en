#!/usr/bin/python
import sys


current_count = 0
current_owner_id = None

def print_current():
    if current_owner_id is not None:
        print "{}\t{}".format(current_owner_id, current_count)

for line in sys.stdin:
    owner_id, count = line.split('\t')
    count = int(count)
    if current_owner_id != owner_id:
        print_current()
        current_owner_id = owner_id
        current_count = count
    else:
        current_count += count
#don't forget the last entry
print_current()