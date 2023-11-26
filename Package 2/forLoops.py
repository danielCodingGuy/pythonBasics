#A simple program using for loops for different purposes.
#author: danielCodingGuy

import time #importing time library for the last example.

#For loop is executed limited number of times instead of infinite times like in the while loop.

for i in range(10): #Loop will print numbers from 1 to 10.
    print(i+1) #With every iteration the number will increase by 1.

for i in range(50,100+1,2): #This loop will print every even number from 50 to 100.
    print(i)

for i in "danielCodingGuy": #This loop will print each letter in the string.
    print(i)

for i in range(10,0,-1): #This loop will countdown from 1 to 10.
    print(i)
    time.sleep(1) #Using time.sleep function it will print one number every second.
print("That's how you count down.") #String will be printed after the full countdown.