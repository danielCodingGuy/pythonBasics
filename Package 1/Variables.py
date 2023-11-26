#Simple program that introduces some of the variables.
#Author: danielCodingGuy

#---STRING
first_name = "Daniel" #This is a variable type called string, it's a string of letters.
last_name = "CodingGuy"
full_name = first_name + " " + last_name #This line is merging two variables to print them together in the next line
print("Hello " + full_name) #This print function that lets us print anything included in it. 
print(type(full_name)) #This line lets us check the datatype of a variable.

#---INT
age = 20 #This is a variable type called integer, it's a variable containing natural numbers.
age += 1
print("Your age is: " + str(age)) #In order to avoid an error we casted int type to string in order to add it to the sentence.
print(type(age))

#---FLOAT
height = 183.5 #This is a variable type called float, it is used to write variables with numbers after the comma.
print("Your height is: " + str(height) + "cm")
print(type(height))

#---BOOL
human = True #This is boolean, its a variable containing the True or False value which can be really useful in creating if statements. 
print("Are you a human: " + str(human))
print(type(human))