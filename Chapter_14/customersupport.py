tickets = {}

while True:
    print("\n1.Create Ticket 2.Close Ticket 3.View 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        tickets[input("ID: ")] = "Open"
    elif ch == "2":
        tickets[input("ID: ")] = "Closed"
    elif ch == "3":
        print(tickets)
    else:
        break
