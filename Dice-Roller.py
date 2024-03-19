import random

def roll_dice():
    roll = random.randint(1, 6)  # Simulates a six-sided die
    return roll

result = roll_dice()
print("You rolled a", result)
