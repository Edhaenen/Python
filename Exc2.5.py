# Exercise 2.5: Operators

#a) Write a Python script to calculate the area of a tringle using Herons's formula
a=float(input("Size of side a: "))
b=float(input("Size of side b: "))
c=float(input("Size of side c: "))

s=(a + b + c)/2
print("the semiperimeter s is: {}".format(s))

area=float((s*(s-a)*(s-b)*(s-c))**0.5)
print('='*40)

print("the area of the triangle is:{0:.2f}".format(area))
