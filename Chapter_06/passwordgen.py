import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(p):
    score = 0
    if any(c.islower() for c in p): score += 1
    if any(c.isupper() for c in p): score += 1
    if any(c.isdigit() for c in p): score += 1
    if any(c in "!@#$%^&*" for c in p): score += 1
    return score

pwd = generate_password(12)
print("Password:", pwd)
print("Strength:", check_strength(pwd), "/4")
