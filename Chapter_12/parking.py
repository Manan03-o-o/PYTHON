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
    
# End of parking.py
# Parking Management
# Features:
# 1. Park a car if slots are available. 
# 2. Exit a car from the parking.
# 3. View current parking status.
# 4. Simple command-line interface for interaction.

# Example Usage
# p = Parking(2)
# p.park("ABC123")  
# p.park("XYZ789")
# p.status()
# p.exit("ABC123")
# p.status()

# Output:   
# Car Parked
# Car Parked
# {'ABC123': 'Parked', 'XYZ789': 'Parked'}
# {'XYZ789': 'Parked'}

