#A simple program using index operators.
#author: danielCodingGuy

name = "danielCodingGuy"

if(name[0].islower): #If first letter of a name is lowercase, capitalize first letter.
    name = name.capitalize()

first_name = name[:5].upper() #This function will create variable containing only the first 5 indexes of name using uppercase.
last_name = name[6:].lower() #This function will create variable containing every letter starting from 6 index using lowercase.
last_character = name[-1] #This function will create variable containing last character from our name.

print(name)
print(first_name)
print(last_name)
print(last_character)