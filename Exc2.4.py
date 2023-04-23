#!/usr/bin/python3

#Exercise 2.4: Sets
"""
#a) sets=immutable

myset={1, 2, [3,4]}

#Causes an error: TypeError: unhashable type: 'list'
#Sets cannot have mutabel items but [3,4] is a mutable list

print("this is my set: {}".format(myset))
"""
#b)
Sprot=set()
print(type(Sprot))
Sprot.add('NP_001304113')

print("this set contains only one element: {}".format(Sprot))
Sprot.add('NP_')

print("this set contains two element: {}".format(Sprot))