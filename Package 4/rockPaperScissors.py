# Simple rock paper scissors game made in Python.
# author: danielCodingGuy.

import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices) # Randomly generated choice for computer.
    player = None

    while player not in choices: # In case where user puts something that is not in choices.
        player = input('Choose between rock, paper and scissors.').lower

    if player == computer: # Function in case of every draw possibility.
        print('computer:', computer)
        print('player', player)
        print("It's a tie.")

    elif player == 'rock': # This one and fuctions below for every win/lose possibility.
        if computer == 'paper':
            print('computer:', computer)
            print('player', player)
            print("You lose.")
        if computer == 'scissors':
            print('computer:', computer)
            print('player', player)
            print("You won.")

    elif player == 'paper':
        if computer == 'scissors':
            print('computer:', computer)
            print('player', player)
            print("You lose.")
        if computer == 'rock':
            print('computer:', computer)
            print('player', player)
            print("You won.")

    elif player == 'scissors':
        if computer == 'rock':
            print('computer:', computer)
            print('player', player)
            print("You lose.")
        if computer == 'paper':
            print('computer:', computer)
            print('player', player)
            print("You won.")

    play_again = input("Want to play again? (yes/no): ").lower

    if play_again != "yes": # If input is not equal to yes -> exit program.
        break
    print("Bye!")