
# Simple Dice Roller
import random

def roll_the_dice(num_sides):
    return random.randint(1, num_sides)

while True:
    print("Enter the number of sides for your dice (type 'x' to quit): ")
    user_input = input()

    if user_input == 'x':
        break

    if user_input.isdigit() and int(user_input) > 0:
        print(f"You rolled {roll_the_dice(int(user_input))}")
    else:
        print("Invalid number")