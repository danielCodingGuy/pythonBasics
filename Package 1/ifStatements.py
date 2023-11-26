#A simple program that uses if statements.
#author: danielCodingGuy

age = int(input("How old are you?: "))

#The first statement in python is always if
if age < 0:
    print("You haven't been born yet!")
#When the first if statement wasn't true, then the program executes next else if statement
elif age >= 18:
    print("You are an adult.")
elif age > 100:
    print("Damn, you are old!")
#The last if statement is always else, its true when all of the other statements were false
else:
    print("You are a child.")