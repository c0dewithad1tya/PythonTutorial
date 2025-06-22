import random

# This script scrambles a list of chess piece names and prints them in a random order
# The list of chess piece names
words = ['bishop', 'pawn', 'knight', 'rook', 'queen', 'king']

print("Welcome to the Chess Piece Scrambler!")

original_word = random.choice(words)
temporary_list = list(original_word)

random.shuffle(temporary_list)
scrambled_word = ''.join(temporary_list)

print("Guess the scrambled word = ", scrambled_word)
user_guess = input("Enter your guess: ")

if user_guess.lower() == original_word:
    print("Congratulations! You guessed it right.")
else:
    print("Sorry, that's not correct.")
    print("The original word is:", original_word)

