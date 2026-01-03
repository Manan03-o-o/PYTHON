chat = []

while True:
    print("\n1.Send 2.Read 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        chat.append(input("Message: "))
    elif ch == "2":
        for m in chat:
            print(m)
    else:
        break
