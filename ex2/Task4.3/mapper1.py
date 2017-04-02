#!/usr/bin/python
import sys

#determine the author who has the biggest number of accepted answers
for line in sys.stdin:
    line = line.strip()
    owner_id, ans_id = line.split()
    print "{}\t{}".format(owner_id, 1)