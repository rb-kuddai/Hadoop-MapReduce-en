#!/usr/bin/python

import sys

prev_word = None #None to distinguish empty lines

def print_prev_word():
    if prev_word is not None:
        print(prev_word)

def is_new_word(word):
    return prev_word != word

for line in sys.stdin:          # For ever line in the input from stdin
    # we don't need value, but I am not sure what will be taken for key if there is no explicit splitter   
    word, value = line.split("\t", 1)
    if is_new_word(word):
        print_prev_word()
        prev_word = word

print_prev_word()#print the last word 
