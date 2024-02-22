# A simple python program that uses abstract classes.
# author: danielCodingGuy

# Abstract classes are classes that contain one or more abstract methods.
# Abstract method is a method that has declaration but no implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car.")

class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle.")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go() # As you will be able to see this method will print nothing cause its our abstract method.
car.go() # Our abstract method is a parent class of classes Car() and Motorcycle() so our child classes will be able to work just fine cause they are not abstract classes.
motorcycle.go()