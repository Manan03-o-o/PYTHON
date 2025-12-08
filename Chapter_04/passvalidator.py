pwd = input("Enter password: ")

rules = [
    any(c.isupper() for c in pwd),
    any(c.islower() for c in pwd),
    any(c.isdigit() for c in pwd),
    any(c in "@#$%&!" for c in pwd),
    len(pwd) >= 8
]

if all(rules):
    print("Strong Password")
else:
    print("Weak Password")
