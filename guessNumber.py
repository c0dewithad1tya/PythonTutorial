'''
    Guess the Number!
    Computer makes a random choice from 1 to 100 and user has to guess the number
    If the guess is higher than the choice then pring too high
    else print too low until user guesses the number
'''
import random

numToGuess = random.randrange(1,100)
userGuess = int(input("Let's play High/Low.\nGuess the number = "))
score = 10
flag = True

while flag and score != 0:
    if numToGuess == userGuess:
        flag = False
        print("You guessed it right!")
        print("Your score is",score)
    elif numToGuess > userGuess:
        print("Too Low")
        score = score - 1
        userGuess = int(input("Guess again = "))
    elif numToGuess < userGuess:
        print("Too High")
        score = score - 1
        userGuess = int(input("Guess again = "))
if score == 0:
    print("You cannot guess anymore. Out of lives!")