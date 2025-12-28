class Hotel:
    def __init__(self):
        self.rooms = {101: "Empty", 102: "Empty", 103: "Empty"}

    def book_room(self, room, name):
        if self.rooms.get(room) == "Empty":
            self.rooms[room] = name
            print("Room Booked")
        else:
            print("Room Occupied")

    def checkout(self, room):
        self.rooms[room] = "Empty"
        print("Checkout Done")

    def status(self):
        for r, s in self.rooms.items():
            print("Room", r, ":", s)

hotel = Hotel()

while True:
    print("\n1.Book 2.Checkout 3.Status 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        hotel.book_room(int(input("Room: ")), input("Name: "))
    elif ch == "2":
        hotel.checkout(int(input("Room: ")))
    elif ch == "3":
        hotel.status()
    else:
        break
