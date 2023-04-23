#!/usr/bin/python3

#1 write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
"""
Numbers=[]

for n in range(1500, 2701):
    if n%7 == 0 and n%5 == 0:
        Numbers.append(n)
print(str(Numbers))
"""
#2 Write a Python program to convert temperatures to and from Celsius and Fahrenheit. 
"""
temp = input("Give the temp you like to convert? (e.g., 45F, 102C etc.): ")
degree = int(temp[:-1])
i_convention = temp [-1]

if i_convention == "C":
    result = int(round(1.8*degree + 32))
    o_convention = "F"
elif i_convention == "F":
    result = int(round((degree - 32)/1.8))
    o_convention = "C"
else:
    print ("Proper convention requered")
    quit()
print("The temperature in {} is {}".format(o_convention, result))
"""

# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

numbers = range(51)

for n in numbers:
    if n%3 == 0:
        n = "Fizz"
        print(n)
    elif n%5 == 0:
        n = "Buzz"
        print(n)
    elif n%5 == 0 and n%3 == 0:
        n = "FizzBuzz"
        print(n)
    print(n)