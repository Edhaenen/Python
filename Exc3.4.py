#!/usr/bin/python3

#a) Print a list of capitals (values)
List_C = {"Belgium":"Brussels", "France":"Paris", "England":"London", "Spain":"Barcelona"}
print("List of Capitals:")
print("="*20)

for v in List_C.values():
    print(v)

#b) 
n = 5
for i in range(n):
    print("* "*i)
for i in range(n,0,-1):
    print("* "*i)
    
#b) nested
n = 5
for i in range(n):
    for j in range(i):
        print("* ",end="")
    print("")
for i in range(n,0,-1):
    for j in range(i):
        print("* ",end="")
    print("")





