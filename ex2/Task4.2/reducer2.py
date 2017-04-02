#!/usr/bin/python
import sys

#I use only one reducer because it will receive output only
#from one person (around 2K which is affordable to do in one reducer)

for line in file('max_user.txt'):
    max_owner_id, rest = line.strip().split()
    sys.stdout.write("{0} -->".format(max_owner_id))
    break

curr_parent_id = None
first_one = True

def print_current():
    if curr_parent_id is None:
        return True
    if first_one:
        sys.stdout.write(" {0}".format(curr_parent_id))
    else:
        sys.stdout.write(", {0}".format(curr_parent_id))
    return False

for line in sys.stdin:
    parent_id = line.strip()
    #ensure uniqueness
    if curr_parent_id != parent_id:
        first_one = print_current()
        curr_parent_id = parent_id

#print the last one
print_current()