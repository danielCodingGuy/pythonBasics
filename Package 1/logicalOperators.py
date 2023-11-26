#A simple program that uses logical operators.
#author: danielCodingGuy

temp = int(input("What is the temperature outside?: "))

#Logical operators are: and, or, not.

if temp>= 0 and temp <=30: #And is true when both arguments are true
    print("The temperature is good today!")
    print("Go outside.")
elif temp < 0 or temp > 30: #Or is true when one of the two arguments is true
    print("Damn, the weather is awful!")
    print("Stay at home.")

#On the example below I added not to the first if statement, the instruction will be always opposite.
#If the instruction would be normally true, with operator: not it will be false.

#if not (temp>= 0 and temp <=30):
#    print("The temperature is good today!")
#    print("Go outside.")