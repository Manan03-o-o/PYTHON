phone = {}

while True:
    print("\n1.Add\n2.Search\n3.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        name = input("Name: ")
        number = input("Number: ")
        phone[name] = number

    elif ch == 2:
        name = input("Search name: ")
        print(phone.get(name, "Not Found"))

    else:
        break
