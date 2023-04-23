#!/usr/bin/python3
#Function to reverse a string

def strg_reverse(str1):
    rstrg1 = ""
    index = len(str1)
    while index > 0:
        rstrg1 += str1[index - 1]
        index -= 1
    return rstrg1


print("Reverse of live desserts = ", end="")
print(strg_reverse("live desserts"))
"""
str = input("Give a string: ")

print("this is the reverse: {}".format(strg_reverse(str)))
"""