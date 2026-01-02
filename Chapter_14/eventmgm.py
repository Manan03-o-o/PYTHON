events = {}

while True:
    print("\n1.Add Event 2.Register 3.View 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        events[input("Event: ")] = []
    elif ch == "2":
        e = input("Event: ")
        if e in events:
            events[e].append(input("Name: "))
    elif ch == "3":
        print(events)
    else:
        break
