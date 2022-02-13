import random
import sys

print("Rock, Paper, Scissors ")

wins = 0
ties = 0
losses = 0

# The main loop for the game
while True:

    # Game score
    # print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    # player input loop
    while True:

        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input().lower()

        # Quit the program
        if playerMove == 'q':
            sys.exit()

        # Break out of the player input loop
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
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
        ties = ties + 1

    elif playerMove == "r" and computerMove == "s":
        print("Rock smashes scissors! You win!")
        wins = wins + 1

    elif playerMove == "r" and computerMove == "p":
        print("Paper covers rock! You lose.")
        losses = losses + 1

    elif playerMove == "s" and computerMove == "r":
        print("Rock smashes scissors! You lose.")
        losses = losses + 1

    elif playerMove == "s" and computerMove == "p":
        print("Scissors cuts paper! You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "s":
        print("Scissors cuts paper! You lose.")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "r":
        print("Paper covers rock! You win!")
        wins = wins + 1
    print()

    while True:

        # Game score
        print("%s Wins, %s Losses, %s Ties\n" % (wins, losses, ties))
        game_over = input("Play again? (y/n):\n")
        if game_over.lower() == "y":

            # Game score
            # print("%s Wins, %s Losses, %s Ties\n" % (wins, losses, ties))
            break
        elif game_over.lower() == "n":
            sys.exit()
        else:
            print("please enter y/n\n")


