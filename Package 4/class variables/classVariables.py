# Simple python program that will use OOP with class variables
# author: danielCodingGuy

from car import Car

car_1 = Car("Honda","Civic",1998,"blue")
car_2 = Car("Subaru","BRZ",2016,"white")

# If you would like to print out the info about wheels you will be able to see that every car that we created by default will have 4 wheels.
print(car_1.wheels)
print(car_2.wheels)

# We can alter the variable to specific object, like on the example below this comment.
car_1.wheels = 2

# We can also print out our class variable from the file car.py by calling the class like on example below.
print(Car.wheels)