#!/usr/bin/python
import sys
import os

#something like hdfs://macallan.inf.ed.ac.uk:8020/data/incredibly/long/path/d1.txt
raw_file_name = os.environ["mapreduce_map_input_file"]
#d1.txt
file_name = raw_file_name.split("/")[-1]

for line in sys.stdin:
    #splitting by the space as everything separated by them is a word
    #for example, this is three terms: got,--lace, "Ryder," Luck"--or
    #remove any whitespace characters as well
    terms = line.split()
    for term in terms:
        #ensure json formatting
        freq_json = '{{"{0}": 1}}'.format(file_name)
        print '{0}\t{1}'.format(term, freq_json)
