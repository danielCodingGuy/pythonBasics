#A simple program using exception handling.
#author: danielCodingGuy

try: #Program executes the try, if something goes sideways then we go through exceptions.
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e: #Exception that prints users action that results in error.
    print(e)
    print("You can't divide by zero.")
except ValueError as e: #Exception that prints users action that results in error.
    print(e)
    print("Enter correct numbers.")
except Exception as e: #Exception that prints error for situations we haven't specified.
    print(e)
    print("Something went wrong, sorry.")
else: #We print our result if every exception does not occur.
    print(result)
finally: #This always executes, no matter if user did everything correct or completely wrong.
    print("If you don't change something up you will see this message.")