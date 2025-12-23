import random

choices = ["rock", "paper", "scissors"]
user = input("Your choice: ")
comp = random.choice(choices)

print("Computer:", comp)

if user == comp:
    print("Draw")
elif (user == "rock" and comp == "scissors") or \
     (user == "paper" and comp == "rock") or \
     (user == "scissors" and comp == "paper"):
    print("You Win")
else:
    print("You Lose")
