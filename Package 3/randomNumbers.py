#A simple program using random numbers.
#author: danielCodingGuy

import random #Importing random module so we can use its functions.

x = random.randint(1,6) #Generating random number in range 1-6.
print(x)

y = random.random(0,1) #Generating random float in range 0-1.
print(y)

RPS = ['rock','paper','scissors'] #List with values that will be picked randomly in next line of code.
z = random.choice(RPS) #Random choice from the list above.
print(z)

cards = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace'] #List containing deck of cards.
random.shuffle(cards) #Shuffle randomly deck of cards.
print(cards)