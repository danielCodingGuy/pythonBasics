#Simple program that uses user inputs.
#author: danielCodingGuy

name = input("What is your name?: ") #Users answer will be the value for variable name.
age = int(input("How old are you year ago?: ")) #Casted users answer to int for easier implementation.
height = float(input("How tall are you?: ")) #Casted to float for more precise answer.

age = age + 1

print("Hello " + name)
print("You are " + str(age) + " years old") #Casted int age to string for display purposes.
print("Your are" + str(height) + "years old") #Casted float height to string for display purposes.
