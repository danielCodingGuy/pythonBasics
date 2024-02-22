# Simple program that uses inheritance made in python.
# author: danielCodingGuy

class Animal: # This will be our parent class that other classes will inherit from.

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal): # That's how you make a class to inherit some functions, in this project our classes will inherit from the class Animal.
    def running(self): # Cause the fish can't run, we can write some functions that are not common enough to not share them between all of the classes and use it only in one class.
        print("This rabbit is running.")

class Fish(Animal):
    def swimming(self):
        print("This fish is swimming.")

class Hawk(Animal):
    def flying(self):
        print("This hawk is flying.")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive) # This line will print inherited value that class Rabbit() got from class Animal().

rabbit.run() # That's the way to use only a function from class Rabbit().