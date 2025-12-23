class Train:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats

    def book(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket Booked")
        else:
            print("No Seats Available")

    def status(self):
        print(f"Train: {self.name}, Seats Left: {self.seats}")

t = Train("Dehradun Express", 3)

while True:
    print("1.Book 2.Status 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        t.book()
    elif ch == "2":
        t.status()
    else:
        break
