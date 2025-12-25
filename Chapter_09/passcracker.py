import random
import string

password = "abc"
attempts = 0

while True:
    guess = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    attempts += 1
    if guess == password:
        print("Cracked:", guess, "Attempts:", attempts)
        break
