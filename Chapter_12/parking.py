class Parking:
    def __init__(self, slots):
        self.slots = slots
        self.parked = {}

    def park(self, car):
        if len(self.parked) < self.slots:
            self.parked[car] = "Parked"
            print("Car Parked")
        else:
            print("Parking Full")

    def exit(self, car):
        self.parked.pop(car, None)

    def status(self):
        print(self.parked)

p = Parking(2)

while True:
    print("\n1.Park 2.Exit 3.Status 4.Exit App")
    ch = input("Choice: ")
    if ch == "1":
        p.park(input("Car No: "))
    elif ch == "2":
        p.exit(input("Car No: "))
    elif ch == "3":
        p.status()
    else:
        break
