#!/usr/bin/python
import sys

prev_col_num = None
is_start = True

for line in sys.stdin: # For every line in the input from stdin
    #the input sorted by col_num and row_num in numerical way
    col_num, row_num, number = map(int, line.split("\t", 2))
    is_new_column = prev_col_num != col_num
    #put the new line with each new col_num, except for the first time
    if is_new_column and not is_start:
        print

    prev_col_num = col_num
    #print number on the same line
    print number,
    is_start = False


