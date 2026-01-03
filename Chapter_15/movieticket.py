movies = {"Avatar": 5, "Jawan": 4}
tickets = {}

while True:
    print("\n1.Book Ticket 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        m = input("Movie: ")
        if movies.get(m, 0) > 0:
            name = input("Name: ")
            movies[m] -= 1
            tickets.setdefault(m, []).append(name)
    elif ch == "2":
        print(tickets)
    else:
        break
