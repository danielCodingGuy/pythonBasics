#A simple python program made for writing text into already existing file.
#author: danielCodingGuy

text = "the guy \n that \n codes"
with open("test.txt","w") as file:
    file.write(text) #Write variable text into file opened using code from line 5.
