# Pseudocode

## Objectives
- Layout the foundation of logic behind the Mastermind game
- Establish naming conventions for variables to be used
- Optimize control flow of algorithm

<br> 


## Meta-Analysis of Approach 

### Big Picture: Create a command line terminal game that allows a player to guess a secret code within a limited number of attempts

<br>

#### Provide appendix of characters we'll be using to construct our code, number of user attempts, code length, and import a module to assist with generating code

```
START:

import random

COLORS =  ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4
```

<br>

#### Generate a 4 color random code
```
Function: def generate_code(): 

Create an empty list called 'code' to store the generated code

Repeat the following steps CODE_LENGTH times:

    Randomly select a color from the COLORS list

    Add the selected color to the 'code' list

Return the generated code as a list of colors
```

<br>

#### Make the user guess the code
```
Function: guess_code():

Start an an infinite loop until a valid guess is made

    Prompt the user to enter a guess and convert it to uppercase, then split it into a list of colors

    Check if the length of the guess is not equal to CODE_LENGTH

        Print an error message indicating that the guess must contain CODE_LENGTH colors

        Continue to the next iteration of the loop to prompt the user for another guess

    Iterate over each color in the guess

        Check if the color is not in the COLORS list

            Print an error message indicating that the color is invalid

            Break out of the inner loop and prompt the user for another guess

    If the inner loop completes without breaking, it means all colors in the guess are valid

        Break out of the outer loop since a valid guess has been made

    Return the valid guess as a list of colors
```

<br>

#### Check the code
```
Function check_code():

    Create an empty dictionary to store the count of each color in the real code

    Initialize a variable to keep track of the number of colors in the correct position

    Initialize a variable to keep track of the number of colors in the incorrect position

    Iterate over each color in the real code

    Check if the color is not already in the color_counts dictionary

        Initialize the count of the color to 0

        Increment the count of the color by 1
    
    Iterate over each color pair in the guess and real code

        Check if the guess color matches the real color in the same position

        Increment the count of colors in the correct position by 1

        Decrement the count of the guess color in the color_counts dictionary by 1

    Iterate over each color pair in the guess and real code again

        Check if the guess color is in the color_counts dictionary and has a count greater than 0

        Decrement the count of colors in the incorrect position by 1

        Decrement the count of the guess color in the color_counts dictionary by 1

    Return the counts of colors in the correct and incorrect positions
```

<br>

#### Tie the game together - provide user with feedback on scoring
```
Print a welcome message indicating the number of tries available

Print the valid colors that can be used for guessing

Generate a random code

Loop for the specified number of tries

    Prompt the user to make a guess

    Check the guess against the generated code

    If the guess is correct (all colors in correct position)

        Print a success message with the number of attempts taken

If the loop completes without breaking (i.e., all tries are exhausted)

Print a message indicating that the player ran out of tries and reveal the correct code

END
```     




            





