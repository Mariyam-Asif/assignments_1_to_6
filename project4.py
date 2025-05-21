# Rock Paper Scissors Game
import random

def play():
    user = input("Choose your move: 'r' for Rock, 's' for Scissors, or 'p' for Paper: ")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return "It's a tie!"
    if is_win(user, computer):
        return "Hurray! You won!"
    return "Aww, you lost!"

def is_win(player, opponent):
    # r > s, p > r, s > p
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True 

print(play())