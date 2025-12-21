import random

num = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess number: "))
    attempts += 1
    if guess > num:
        print("Too High")
    elif guess < num:
        print("Too Low")
    else:
        print("Correct in", attempts, "attempts")
        break
