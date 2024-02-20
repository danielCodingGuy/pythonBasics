# Simple program using object oriented programming(OOP) in Python.
# author: danielCodingGuy.

from car import Car

car_1 = Car("Honda","Civic",1998,"blue")
car_2 = Car("Subaru","BRZ",2016,"white")

# We can print any info about a car like this, in this example we are going to print only the model of car_1.
print(car_1.model)

car_1.drive()
car_2.stop()

