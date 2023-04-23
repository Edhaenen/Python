#!/usr/bin/python3

#a) new list with only even elements
GivenList = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Return = [index for index in GivenList if index % 2 == 0]
print("only even list: {}".format(Return))

#b) ages for a given list of years

BirthYear = [1990, 1995, 1990, 1991, 1992, 1991, 1988]
Ages = [2023-year for year in BirthYear]
print("the age is: {}".format(Ages))