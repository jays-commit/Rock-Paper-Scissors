import random
import sys
from enum import IntEnum

wins = 0
losses = 0
ties = 0


class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


print("Rock, Paper Scissors")


def player_selection():
    print("Enter your move: rock[1] paper[2] scissors[3]] ")
    player_move = int(input())
    selection = player_move
    action = Action(selection)
    return action
    # choices = [f"{action.name}[{action.value}]" for action in Action]
    # choices_str = ", ".join(choices)
    # selection = int(input(f"Enter a choice ({choices_str}): \n"))
    # action = Action(selection)
    # return action


def computer_selection():
    selection = random.randint(1, 3)
    action = Action(selection)
    return action


def determine_winner(player_action, computer_action):
    global wins
    global losses
    global ties

    print(f"{player_action.name} versus {computer_action.name}")
    print(f"You chose {player_action.name}, computer chose {computer_action.name}\n")

    if player_action == computer_action:
        print(f"player and computer both chose {player_action.name} it is a tie ")
        ties = ties + 1

    elif player_action == Action.Rock and computer_action == Action.Scissors:
        print("Rock smashes scissors! You win!")
        wins = wins + 1
    elif player_action == Action.Rock and computer_action == Action.Paper:
        print("Paper covers rock! You lose.")
        losses = losses + 1
    elif player_action == Action.Scissors and computer_action == Action.Rock:
        print("Rock smashes scissors! You lose.")
        losses = losses + 1
    elif player_action == Action.Scissors and computer_action == "paper":
        print("Scissors cuts paper! You win!")
        wins = wins + 1
    elif player_action == Action.Paper and computer_action == Action.Scissors:
        print("Scissors cuts paper! You lose.")
        losses = losses + 1
    elif player_action == Action.Paper and computer_action == Action.Rock:
        print("Paper covers rock! You win!")
        wins = wins + 1


while True:

    try:
        player_action = player_selection()

    except ValueError as e:
        range_str = f"[0, {len(Action) }]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = computer_selection()
    determine_winner(player_action, computer_action)


    while True:

        # Game score
        print("\n%s Wins, %s Losses, %s Ties\n" % (wins, losses, ties))
        game_over = input("Play again? (y/n):\n")
        if game_over.lower() == "y":
            # Game score
            # print("%s Wins, %s Losses, %s Ties\n" % (wins, losses, ties))
            break

        elif game_over.lower() == "n":
            sys.exit()
        else:
            print("please enter y/n\n")
