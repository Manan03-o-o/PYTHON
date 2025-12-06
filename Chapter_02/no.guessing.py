import random

num = random.randint(1, 50)

while True:
    guess = int(input("Guess: "))
    if guess == num:
        print("Correct!")
        break
    elif guess > num:
        print("Too high!")
    else:
        print("Too low!")
print("Game over.")
print("The number was:", num)
print("Thanks for playing!")
print("Goodbye!")
print("Have a great day!")
print("Bye!")
print("See you next time!")
