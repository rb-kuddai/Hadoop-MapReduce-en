#!/usr/bin/python

import sys


for line in sys.stdin:
    row_num, numbers = line.split("\t", 1)
    for col_num, number in enumerate(numbers.split()):
        print("{0}\t{1}\t{2}".format(col_num, row_num, number))