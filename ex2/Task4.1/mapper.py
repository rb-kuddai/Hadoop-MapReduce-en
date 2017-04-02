#!/usr/bin/python
import sys
import re
import heapq

N = 10
top_questions = [(0, None)] * N
heapq.heapify(top_questions)

#post id must be unique key, so we can do the staff on mapper
#as we are not afraid that it will appear somewhere else

for line in sys.stdin:
    pairs = re.findall(r'\s+([^\s]+)="([^"]+)"', line)
    post = dict(pairs)
    #question
    if post["PostTypeId"] == "1":
        view_count = int(post["ViewCount"])
        heapq.heappushpop(top_questions, (view_count, post["Id"]))

#clean from initial None entries if any of them are left
top_questions = filter(lambda x: x[1] is not None, top_questions)
for view_count, post_id in top_questions:
    print "{}\t{}".format(post_id, view_count)

