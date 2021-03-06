from os import system, name
from Game import Game
from time import sleep

# Constants
VALID_INPUTS = [1, 2, 3, 4]
N = 4


# Function to clear the screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Clear the screen and start the game
clear()
g = Game(N)
g.start()
print("\tNUMBERS FOR MOVING : \n\nLeft - 1\nRight - 2\nUp - 3\nDown - 4\n\nPress enter to start ...\n\n")
input()


while True:        # loop till the game is won or lost
    clear()            # Clear the screen
    g.print_board()         # Print the current board

    inp = int(input("\n Enter { 1 - 4 } : "))

    if inp not in VALID_INPUTS:        # Check if input is valid
        print("Enter a valid input between 1 and 4...")
        sleep(1)

    else:
        result = g.move(inp)        # Move the cells in input direction

        if result == 1:
            print("\nYou Won!")
            break
        elif result == -1:
            print("\nYou Lost!")
            break
