import random

rps = ['rock', 'paper', 'scissor']
print("Let's play Rock Paper Scissor")

winning_combinations = {
    'rock': 'scissor',
    'paper': 'rock',
    'scissor': 'paper'
}

while True:
    user_input = input("What do you choose? (type 'end' to quit) ").lower()
    if user_input == 'end':
        break
    if user_input not in rps:
        print("Invalid choice, please choose rock, paper, or scissor.")
        continue

    computer_input = random.choice(rps)
    print("Computer chose", computer_input)

    if user_input == computer_input:
        print("Tied! Play again!")
    elif winning_combinations[user_input] == computer_input:
        print("You Win!")
    else:
        print("Computer Wins!")
