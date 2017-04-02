#!/usr/bin/python

import sys
import re
#take output of the task_8 as its input
for line in sys.stdin:
    name, raw_marks = line.split(" --> ", 1)
    #get marks as the list of tuples of strings
    marks =  re.findall("\((.+?),(\d+)\)", raw_marks)
    num_marks = len(marks)
    if num_marks <= 4:
        continue
    #total student score - float
    score = reduce(lambda res, x: res + int(x[1]), marks, 0.0)
    avg_score = score / num_marks
    print "{0}\t{1}".format(avg_score, name)
