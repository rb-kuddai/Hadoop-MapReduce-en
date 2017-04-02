#!/usr/bin/python
import sys

#filtering all IDs of accepted answers
#where the owner id equals to the ID of the author with
#the biggest number of accepted answers

max_owner_id = None
for line in file('max_user.txt'):
    max_owner_id, rest = line.strip().split()
    break

for line in sys.stdin:
    line = line.strip()
    owner_id, ans_id = line.split()
    if owner_id == max_owner_id:
        print ans_id