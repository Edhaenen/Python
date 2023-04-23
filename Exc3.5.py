#!/usr/bin/python3
#a) write a script to get the largest number from a list

a = [23, 15, 26, 17, 2, 30, 10]

largest = 0
for n in a:
    if n >= largest:
        largest = n
    print("Loop:\t{}\t{}".format(n,largest))
print("-"*20)
print("this is the largest number: {}".format(largest))
print("="*10)
#b) write a script to calculate the sum and average of n integer numbers given by the user (input 0 tot finish)


print("\nEnter integers to calculate sum and average.\nInput 0 to exit.")
count = 0
sum = 0.0
number = 1

while number != 0:
    number = int(input(""))
    sum = sum + number
    count += 1
print("Calculating sum and average for the above numbers:")
average = sum/(count - 1)
print("sum = {}\ncount = {}\naverage = {}\n".format(sum,count-1,average))
print("="*10)





#c) count number of strings lenght 2 or more and first and last character are same
ListWords=["abc","xyz", "aba", "1221","ah", "aha"]


count = 0
result = []
for ele in ListWords:
    if len(ele) > 1 and ele[0]== ele[-1]:
        count +=1
        result.append(ele)

print ("Number of strings: {}".format(count))
print ("List of these words: {}".format(result))
        

        
  