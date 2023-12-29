#A simple python program that uses file reading method.
#author: danielCodingGuy

try:
    with open('test.txt') as a file: #For this to work you will need to create a text file.
        print(file.read()) #If file exists the program will print out the content of the file.
except: FileNotFoundError: #If file cannot be found in the selected directory program will print out that "File cannot be found".
    print("That cannot be found.")
