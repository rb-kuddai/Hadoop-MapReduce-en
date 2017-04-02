#!/usr/bin/python
import sys
import re

max_owner_id = None
for line in file('max_user.txt'):
    max_owner_id, rest = line.strip().split()
    break

for line in sys.stdin:
    pairs = re.findall(r'\s+([^\s]+)="([^"]+)"', line)
    post = dict(pairs)
    if "OwnerUserId" not in post:
        continue
    if post["PostTypeId"] == "2" and post["OwnerUserId"] == max_owner_id:
        parent_id = post["ParentId"]
        print parent_id