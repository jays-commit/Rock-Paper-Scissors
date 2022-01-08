import random
import sys
import enum

wins = 0
losses = 0
ties = 0

print("Rock, Paper Scissors")

while True:

    possible_moves = ["rock", "paper", "scissors"]
    print("Enter your move: rock paper scissors or quit ")
    player_move = input().lower()

    if player_move == "quit":
        sys.exit()

    computer_move = random.choice(possible_moves)
    print(f"{player_move.upper()} versus {computer_move.upper()}")
    print(f"You chose {player_move} computer chose {computer_move}\n")

    if player_move == computer_move:
        print(f"player and computer both chose {player_move} it is a tie ")

    elif player_move == "rock" and computer_move == "scissors":
        print("Rock smashes scissors! You win!")
        wins = wins + 1
    elif player_move == "rock" and computer_move == "paper":
        print("Paper covers rock! You lose.")
        losses = losses + 1
    elif player_move == "scissors" and computer_move == "rock":
        print("Rock smashes scissors! You lose.")
        losses = losses + 1
    elif player_move == "scissors" and computer_move == "paper":
        print("Scissors cuts paper! You win!")
        wins = wins + 1
    elif player_move == "paper" and computer_move == "scissors":
        print("Scissors cuts paper! You lose.")
        losses = losses + 1
    elif player_move == "paper" and computer_move == "rock":
        print("Paper covers rock! You win!")
        wins = wins + 1
    while True:

        game_over = input("Play again? (y/n):\n")
        if game_over.lower() == "y":

            # Game score
            print("%s Wins, %s Losses, %s Ties\n" % (wins, losses, ties))
            break
        elif game_over.lower() == "n":
            sys.exit()
        else:
            print("please enter y/n\n")
