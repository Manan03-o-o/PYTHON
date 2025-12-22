import random

pos = 0
snakes = {17:7, 54:34}
ladders = {3:22, 20:38}

while pos < 100:
    dice = random.randint(1,6)
    pos += dice
    pos = snakes.get(pos, pos)
    pos = ladders.get(pos, pos)
    print("Position:", pos)

print("You Win!")
