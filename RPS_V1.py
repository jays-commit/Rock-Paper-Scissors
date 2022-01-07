import random
import sys

print("Rock, Paper, Scissors ")

wins = 0
ties = 0
losses = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')
    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove:
        print("Tie")
        ties = ties +1

    elif playerMove == "r" and computerMove == "s":
        print("Win")
        wins = wins + 1

    elif playerMove == "r" and computerMove == "p":
        print("Loss")
        losses = losses + 1

    elif playerMove == "s" and computerMove == "r":
        print("Loss")
        losses = losses + 1

    elif playerMove == "s" and computerMove == "p":
        print("Win")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "s":
        print("Loss")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "r":
        print("Win")
        wins = wins + 1
