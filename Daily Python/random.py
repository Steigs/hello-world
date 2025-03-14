# page 180, importing the random class

from random import randint
print(randint(1,6))

import random

def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)  # Simulates rolling a six-sided die
        results.append(roll)
    return results

def main():
    num_dice = int(input("How many dice would you like to roll? "))
    rolls = roll_dice(num_dice)
    print("You rolled:", rolls)

if __name__ == "__main__":
    main()
