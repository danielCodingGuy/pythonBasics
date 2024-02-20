# Here is our second file that Object Oriented programming will be using.

class Car:

    def __init__(self, manufacturer, model, year, color):
        self.make = manufacturer
        self.model = model
        self.year = year
        self.color = color

    def drive(self): # This function will print out in the main file that the car is driving, for full clarity I added the info about model of the car
        print("This " + self.model + " is driving.")
    def stop(self):
        print("This " + self.model + " is stopped.")