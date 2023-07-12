from random import randint
number = randint(1, 100)
question = "what's your guess?"
print("I've choses a number from 1 to 100, try to guess it")
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

   
