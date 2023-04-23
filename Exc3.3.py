#!/usr/bin/python3

#a) Fibonacci series between 0 to 50

x,y=0,1
while x < 50:
    r = x + y
    print("{} ({}+{})".format(x,x,y,r))
    x = y
    y = r

#b) guess a number between 1 to 9

import random
target_num = random.randint(1,9)
guess_num = 0
while target_num != guess_num:
        guess_num = int(input("\nGuess a number between 1 and 9: "))
print("\nYES! {} that's the number!".format(guess_num))    

