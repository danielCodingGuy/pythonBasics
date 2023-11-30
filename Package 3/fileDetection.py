#A simple program using file detection.
#author: danielCodingGuy

import os
path = "C:\\Users\\Daniel\\Desktop\\test.txt"

if os.path.exists(path): #This function checks if the path to the file exists.
    print("That location exists!")
    if os.path.isfile(path): #This function checks if the file in variable path exists.
        print("There is your file!")
    elif os.path.isdir(path): #This function checks if the directory in variable path exists.
        print("That is a directory!")
else:
    print("That location doesn't exist!")