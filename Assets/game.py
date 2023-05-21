# This module implements pseudo-random number generators for various distributions
import random

# Constants Defining all the colors that we'll be using, number of user attempts, and code length
COLORS =  ["R", "G", "B", "Y", "w", "O"]
TRIES = 10
CODE_LENGTH = 4

# Generate a 4 color random code
def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    
    return code

# Make the user guess the code
def guess_code():
    while True:
        guess = input("Guess:").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again")
            
                break
            else:
                break

# Compare the guess

# Tie the game together - provide user with feedback on scoring
