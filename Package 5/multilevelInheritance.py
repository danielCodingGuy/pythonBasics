# A simple python program that uses multilevel inheritance.
# author: danielCodingGuy

class Organism: # This one we could call grandparent of the class Dog() as it inherits values from already inheriting class.
    alive = True

class Animal(Organism): # That's the parent class of class Dog().
    def eat(self):
        print("This animal is eating.")

class Dog(Animal): # To inherit values from the two classes above we can just inherit from the class that's already inheriting values from their parent class.
    def bark(self):
        print("This dog is barking.")

dog = Dog()
print(dog.alive) # By printing something from the grandparent class we can check if everything runs according to plan.
dog.eat() # The same as above goes to this one.