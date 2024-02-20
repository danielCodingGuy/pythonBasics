# Simple python program using class variable.

class Car:
    wheels = 4 # This is class variable, every single one of cars from class 'Car' will have by defaul four wheels, they are initialized outside of our constructor - Thats the difference between instance variables and class variables.

    # Here in our constructor we are initializing instance variables.
    def __init__(self,manufacturer,model,year,color):
        self.manufacturer = manufacturer # This and next three are instance variables, we are initializing them inside constructor.
        self.model = model  # Every variable here can have their own unique values.
        self.year = year
        self.color = color