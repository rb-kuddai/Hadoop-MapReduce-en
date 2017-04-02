#!/usr/bin/python

import sys

for line in sys.stdin:
    tag, data = line.split(" ", 1)

    if   tag == "student":
        student_ID, name = data.split()
        print "{0}\t{1}\t{2}".format(student_ID.strip(), tag.strip(), name.strip())
    elif tag == "mark":
        subject_ID, student_ID, score = data.split()
        print "{0}\t{1}\t{2} {3}".format(student_ID.strip(), tag.strip(), subject_ID.strip(), score.strip())

