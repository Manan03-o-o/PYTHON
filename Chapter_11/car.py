class CarRental:
    def __init__(self):
        self.cars = {"Swift": True, "BMW": True}

    def rent(self, car):
        if self.cars.get(car):
            self.cars[car] = False
            print("Car Rented")
        else:
            print("Not Available")

    def return_car(self, car):
        self.cars[car] = True

cr = CarRental()

while True:
    print("\n1.Rent 2.Return 3.Status 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        cr.rent(input("Car: "))
    elif ch == "2":
        cr.return_car(input("Car: "))
    elif ch == "3":
        print(cr.cars)
    else:
        break
