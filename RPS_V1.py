import random
import sys

print("Rock, Paper, Scissors ")

wins = 0
ties = 0
losses = 0

# The main loop for the game
while True:

    # Game score
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    # player input loop
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

