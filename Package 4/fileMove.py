#Simple python program using file moving method.
#author: danielCodingGuy

import os

source = "test.txt"
destination = "C:\\Users\\Daniel\\Desktop\\test.txt"

try:
    if os.path.exists(destination): #If file already exists in our destination.
        print("There is already file there.")
    else: #Else if file does not exist in our destination move our source there.
        os.repleace(source,destination)
        print(source + "was moved.")
except FileNotFoundError: #Exception if the file cannot be found.
    print(source + "was not found.")
