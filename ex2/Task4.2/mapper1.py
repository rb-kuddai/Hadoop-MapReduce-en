#!/usr/bin/python
import sys
import re

#here I account that if the person answered on the same question
#multiple times then I acknowledge each such answer as separate answer.
#Because it is unclear from the task whether I should account it or not.
#There is no such problems with accepted answer though.
#Moreover, in our dataset, it seems that both approaches produce the same result. But
#in general case they should be different ones.
#In case, of other interpretation (if I should account only one answer for the same question from the same person)
#then I would just add another MapReduce job before this one (so we can call it job0) and make reduce side join
#on ParentId to exclude repetitions (I do something like that in the next task).

#The persons could have a significant amount of answers (~20K).
#So determining who has the most answers on reducer side  and keeping all the answers
#at the same time will require approximately number_of_reducers * average_number_of_answers memory.
#So I use several map reduce jobs. Finding the person with most answers in the first pass and
#projecting all the answers of this person in the second job.


for line in sys.stdin:
    pairs = re.findall(r'\s+([^\s]+)="([^"]+)"', line)
    post = dict(pairs)
    if "OwnerUserId" not in post:
        continue
    if post["PostTypeId"] == "2":
        owner_id = post["OwnerUserId"]
        print "{}\t{}".format(owner_id, 1)