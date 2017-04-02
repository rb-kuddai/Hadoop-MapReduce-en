#!/usr/bin/python
#I used the code from lecture for reducer
#because it just counts the number of the same keys separated from values by tab
import sys

prev_word = ""
value_total = 0
word = ""

def is_new_word(word):
    return prev_word != word

def print_previous():
    if prev_word:  # write result to stdout
        print("{0}\t{1}".format(prev_word, value_total))

for line in sys.stdin:          # For ever line in the input from stdin
    word, value = line.split("\t", 1)
    value = int(value)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if is_new_word(word):
        print_previous()

        value_total = value
        prev_word = word
    else:
        value_total += value

print_previous()