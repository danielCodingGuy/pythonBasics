#A simple program that uses while loop.
#author: danielCodingGuy

name = ""

#While length of the name is 0 the while loop will keep asking for name till user enters his name.
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)