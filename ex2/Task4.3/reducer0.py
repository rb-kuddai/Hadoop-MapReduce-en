#!/usr/bin/python
import sys

curr_ans_id = None
is_accepted = False

#the pair of accepted answer and owner_id is alway unique

for line in sys.stdin: # For every line in the input from stdin
    ans_id, post_type_id, rest = line.strip().split('\t')
    is_new_id = curr_ans_id != ans_id
    if is_new_id:
        curr_ans_id = ans_id
        is_accepted = post_type_id == "1"
        #there is no need to print new accepted line
        #and there is no need to print reject point
        continue

    if is_accepted:
        owner_id = rest
        print "{}\t{}".format(owner_id, curr_ans_id)



