from random import randint, seed

# The randint(a,b) function return a pseudorandom number between a and b, including both.
# The seed() function defines a new seed for pseudorandom numbers.

# This function defines a die roll. If no specific side is defined, it 'rolls' a six-sided die.
  
def die(sides=6):
    seed()
    result = randint(1, sides)
    return result

# This function defines a dice roll. 
# If no specific side and number of dies are defined, it 'rolls' a six-sided die.
#Returns a list of ints with the dice rolls.

def dice(number_of_die=1, sides=6):
    rolls = []
    for roll in range(0, number_of_die):
        rolls.append(die(sides))
    return rolls