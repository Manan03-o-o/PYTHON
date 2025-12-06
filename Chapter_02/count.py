s = input("Enter string: ")

letters = digits = special = 0

for c in s:
    if c.isalpha(): letters += 1
    elif c.isdigit(): digits += 1
    else: special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special chars:", special)
