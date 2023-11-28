#A simple program using string formats.
#author: danielCodingGuy

number = 1000
first_word = "daniel"
second_word = "coding"
third_word = "guy"

#String formats are used in order to give users more control when displaying output.
#Example with inserting variables
print("{0} is {1} hard or hardly {1} type of {2}".format(first_word,second_word,third_word)) #We are using indexes so the program knows which variable should be printed.
#Example with formating the values
print("The number is {:.3f}".format(number)) #This will print three numbers after comma(1000.000).
print("The number is {:,}".format(number)) #This will insert comma after thousands(1,000).
print("The number is {:b}".format(number)) #This will format our number from decimal to binary.
print("The number is {:o}".format(number)) #This will format our number from decimal to octal.
print("The number is {:X}".format(number)) #This will format our number from decimal to hexadecimal.
print("The number is {:E}".format(number)) #This will format our number in scientific notation.
