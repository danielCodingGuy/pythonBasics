#A simple program using variable scope.
#author: danielCodingGuy

#We use variable scope to store a variable only in specified area of the program.

name = "CodingGuy" #This variable is using global scope, it can be accessed anywhere in the program.

def display_name():
    name = "Daniel" #This variable can't be accessed outside of this function.
    print(name)

display_name() #This will display our local variable used only in the function.
print(name) #This will print global variable, because it can only access the global function name.