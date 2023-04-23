#!/usr/bin/python
# a) Ask for the input from the user and print this in upper- en lowercase
"""
str_in= input("Enter a word or sentence: ")
print("Uppercase: {}\n" 
        "Lowercase: {}"
        .format(str_in.upper(),str_in.lower()))
"""
"""
#b) Sequence as input, find motif and show the position of the motif in the sequence

seq= input("Enter a sequence: ")
motif = input ("Enter a motif to search for: ")
find_pos= seq.find(motif)+1
find_index= seq.index(motif)
print("Motif found at position: {}; Motif found at index: {}".format(find_pos, find_index))
"""
#c) Cleavage site
seq= input("Enter a sequence: ")
Cleavage = input ("Enter the cleavage site: ")
print(seq.split(Cleavage))