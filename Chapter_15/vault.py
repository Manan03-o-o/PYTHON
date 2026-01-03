vault = {}

while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        vault[input("Site: ")] = input("Password: ")
    elif ch == "2":
        print(vault)
    elif ch == "3":
        vault.pop(input("Site: "), None)
    else:
        break
