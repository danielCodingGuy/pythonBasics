#A simple program using nested loops to print a rectangle.
#author: danielCodingGuy

rows = int(input("How many rows?: ")) #User inputs the length of the rectangle.
columns = int(input("How many columns?: ")) #User inputs the width of the rectangle.
symbol = input("Enter a symbol to use: ") #User inputs the symbol that will be usedf to print the rectangle.

for i in range(rows): #This loop prints the rows.
    for j in range(columns): #This loop prints the columns.
        print(symbol, end="")
    print()