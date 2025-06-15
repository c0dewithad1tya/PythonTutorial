import random

#This is a code to genrate random number

dice_roll = random.randint(1,6)

if dice_roll == 6:
    print('Oh! You get another dice roll')
    print(dice_roll)
    dice_roll = random.randint(1,6)
print(dice_roll)
