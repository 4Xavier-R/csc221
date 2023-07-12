from random import randint
from gasp.utils import read_yesorno
while True:
    
    question = "what's your guess?"
    rquestion = "What would you like the range to be. 1 to ?"
    r = (int(input(rquestion)))
    number = randint(1, r)
    print("I've choses a number from 1 to " + str(r) + ", try to guess it")
    guess = 0
    guesses = 0
    while True:
        guess = (int(input(question)))
        if guess < number:
            print("The number is higher than that")
            guesses = guesses +1
        if guess > number:
            print("The number is lower than that")
            guesses = guesses +1
        if guess == number:
            print("That's Correct!")
            guesses = guesses +1
            print("Your total number of guesses was " + str(guesses))
            break
    if read_yesorno("Would you like to play again?"):
        print("Alright")
    else:
        break
