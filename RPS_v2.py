import random
import sys
import enum

print("Rock, Paper Scissors")

while True:

    possible_moves = ["rock", "paper", "scissors"]
    player_move = input('Enter your move: rock paper scissors or quit').lower()

    if player_move == "quit":
        sys.exit()

    computer_move = random.choice(possible_moves)
    print(f"You chose {player_move} and the computer chose {computer_move}")
