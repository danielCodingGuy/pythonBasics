# A simple quiz game made in Python.
# author: danielCodingGuy

#------------------------
# This function is our base game function, it prints the questions and borrows other functions below in order to work properly.
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('---------------------')
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)

#------------------------
# This function checks answers of the user.
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else: 
        print("Wrong.")
        return 0

#------------------------
# This function calculates the score of the user.
def display_score(correct_guesses, guesses):
    print('---------------------')
    print('Results')
    print('---------------------')
    print()
    
    print("Answers: " end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: " end="")
    for i in guesses:
        print(questions.get(i), end="")
    print()

    score = int((correct_guesses / len(questions))*100)
    print('Your score is: ' + str(score)+"%")

#------------------------
# This function checks if user wants to play again.
def play_again():
    response = input('Do you want to play again? (yes/no)')
    response = response.upper()

    if response == 'YES':
        return True
    else:
        return False

#------------------------
# There we have our questions and answers for specific questions.
questions = {
    "Who created Python?: ": "A",
    "Which year was Python created in?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A" 
}
# And here we have four answers for the questions, only one is true.
options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Joe Rogan", "D. Monty Python"]
    ["A. 1988", "B. 1991", "C. 2000", "D. 2008"]
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"]
    ["A. True", "B. False", "C. Sometimes", "Monty Python"]
]

#-----------------------
new_game() # This function starts the new game.

while play_again(): # If play_again() is True.
    new_game() # Start the new game.

print("Bye.")