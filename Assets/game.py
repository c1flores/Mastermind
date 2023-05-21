# This module implements pseudo-random number generators for various distributions
import random

# Constants Defining all the colors that we'll be using, number of user attempts, and code length
COLORS =  ["R", "G", "B", "Y", "W", "O"]
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
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again")
                break

        else:
            break

    return guess

# Compare the guess
def check_code(guess, real_code):
    color_counts = {}
    correct_position = 0
    incorrect_position = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_position += 1
            color_counts[guess_color] -= 1
        
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_position -= 1
            color_counts[guess_color] -= 1

    return correct_position, incorrect_position

# Tie the game together - provide user with feedback on scoring
def game():
    print(f"Welcome to Mastermind, you have {TRIES} tries to guess the code...")
    print("The valid colors are", *COLORS)
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_position, incorrect_position = check_code(guess, code)

        if correct_position == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct positions: {correct_position} | Incorrect Positions: {incorrect_position}")

    else:
        print("You ran out of tries, the code was:", *code)

if __name__ == "__main__":
    game()