passwords = {}

while True:
    print("1.Add 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        site = input("Site: ")
        pwd = input("Password: ")
        passwords[site] = pwd
    elif ch == "2":
        for s, p in passwords.items():
            print(s, p)
    else:
        break
