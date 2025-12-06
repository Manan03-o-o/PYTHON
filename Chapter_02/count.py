s = input("Enter string: ")

letters = digits = special = 0

for c in s:
    if c.isalpha(): letters += 1
    elif c.isdigit(): digits += 1
    else: special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special chars:", special)
print("Total chars:", len(s))
print("Total words:", len(s.split()))
print("Total lines:", s.count('\n') + 1)
print("Whitespace chars:", sum(1 for c in s if c.isspace()))
print("Uppercase letters:", sum(1 for c in s if c.isupper()))
print("Lowercase letters:", sum(1 for c in s if c.islower()))
print("Vowels:", sum(1 for c in s.lower() if c in 'aeiou'))
print("Consonants:", sum(1 for c in s.lower() if c.isalpha() and c not in 'aeiou'))
