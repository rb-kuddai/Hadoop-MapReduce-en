#!/usr/bin/python
import sys
import heapq

N = 10
top_questions = [(0, None)] * N
heapq.heapify(top_questions)

for line in sys.stdin:
    line = line.strip()
    post_id, view_count = line.split('\t')
    view_count = int(view_count)
    heapq.heappushpop(top_questions, (view_count, post_id))

#clean from initial None entries if any of them potentailly exist (not in this task I guess)
top_questions = filter(lambda x: x[1] is not None, top_questions)
for view_count, post_id in top_questions:
    print "{},\t{}".format(post_id, view_count)