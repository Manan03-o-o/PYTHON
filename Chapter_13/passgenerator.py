def strength(p):
    s=0
    s+=any(c.islower() for c in p)
    s+=any(c.isupper() for c in p)
    s+=any(c.isdigit() for c in p)
    s+=any(c in "!@#$" for c in p)
    return s

p=input("Password: ")
print("Strength:", strength(p),"/4")
