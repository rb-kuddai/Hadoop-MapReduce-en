#!/usr/bin/python
import sys

for line in file('max_user.txt'):
    max_owner_id, total_count = line.strip().split()
    sys.stdout.write("{0} --> {1}, ".format(max_owner_id, total_count))
    break

curr_ans_id = None
first_one = True

def print_current():
    if curr_ans_id is None:
        return True
    if first_one:
        sys.stdout.write(" {0}".format(curr_ans_id))
    else:
        sys.stdout.write(", {0}".format(curr_ans_id))
    return False

for line in sys.stdin:
    ans_id = line.strip()
    #ensure uniqueness
    if curr_ans_id != ans_id:
        first_one = print_current()
        curr_ans_id = ans_id

#print the last one
print_current()