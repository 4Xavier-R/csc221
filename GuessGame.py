from random import randint
from gasp.utils import read_yesorno
while True:
    
    question = "what's your guess?\n"
    rquestion = "What would you like the range to be. 1 to ?\n"
    r = (int(input(rquestion)))
    number = randint(1, r)
    print("I've thought of a number between 1 and " + str(r) + ", try to guess it.")
    guess = 0
    guesses = 0
    while True:
        guess = (int(input(question)))
        guesses += 1
        if guess < number:
            print("The number is higher than that.\n")
        if guess > number:
            print("The number is lower than that.\n")
        if guess == number:
            print("That's Correct!")
            print("Your total number of guesses was " + str(guesses))
            break
    if read_yesorno("Would you like to play again?\n"):
        print("Alright")
    else:
        break
