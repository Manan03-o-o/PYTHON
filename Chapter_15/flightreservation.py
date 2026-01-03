flights = {"AI101": 3, "AI202": 2}
booked = {}

while True:
    print("\n1.Book 2.Status 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        f = input("Flight: ")
        if flights.get(f, 0) > 0:
            name = input("Passenger: ")
            flights[f] -= 1
            booked.setdefault(f, []).append(name)
            print("Booked")
    elif ch == "2":
        print("Flights:", flights)
        print("Passengers:", booked)
    else:
        break
