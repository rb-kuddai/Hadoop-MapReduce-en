#!/usr/bin/python
import sys
import re

#perform reducer side join on accepted answer id and answer id
for line in sys.stdin:
    pairs = re.findall(r'\s+([^\s]+)="([^"]+)"', line)
    post = dict(pairs)
    if post["PostTypeId"] == "1":
        #question
        if "AcceptedAnswerId" not in post:
            continue
        accepted_id = post["AcceptedAnswerId"]
        print "{}\t{}\tEmpty".format(accepted_id, post["PostTypeId"])
    if post["PostTypeId"] == "2":
        #answer
        if "OwnerUserId" not in post:
            continue
        owner_id = post["OwnerUserId"]
        post_id  = post["Id"]
        print "{}\t{}\t{}".format(post_id, post["PostTypeId"], owner_id)

