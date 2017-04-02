#!/usr/bin/python
import sys

curr_student_ID = None
curr_student_name = None
is_name_printed = False
is_start = True

for line in sys.stdin: # For every line in the input from stdin
    #sorted by student_id and
    #sorted by tag reversely, so we have student record before his mark record
    student_ID, tag, record = line.split("\t", 2)

    is_new_student = curr_student_ID != student_ID
    #clean record from the tabs and spaces
    record = record.strip()

    if is_new_student:
        #if it is new student then it starts from student record
        #update current student
        curr_student_ID = student_ID
        curr_student_name = record
        is_name_printed = False
        #wait for the mark
        continue

    #see the same student, must be a mark record

    if not is_name_printed:
        #put new line before student name, except in the case of start
        if not is_start:
            print

	sys.stdout.write("{0} -->".format(curr_student_name))
        is_name_printed = True

    #printing new mark on the same line
    subject_ID, score = record.split()

    sys.stdout.write(" ({0},{1})".format(subject_ID, score))
    #we have already printed one student mark, it is not a start anymore
    is_start = False




