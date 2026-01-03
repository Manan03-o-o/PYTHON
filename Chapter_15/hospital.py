class Hospital:
    def __init__(self):
        self.doctors = {}
        self.appointments = []

    def add_doctor(self, name, dept):
        self.doctors[name] = dept

    def book(self, patient, doctor):
        if doctor in self.doctors:
            self.appointments.append((patient, doctor))
            print("Appointment Booked")

    def view(self):
        for a in self.appointments:
            print("Patient:", a[0], "Doctor:", a[1])

h = Hospital()

while True:
    print("\n1.Add Doctor 2.Book Appointment 3.View 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        h.add_doctor(input("Doctor: "), input("Dept: "))
    elif ch == "2":
        h.book(input("Patient: "), input("Doctor: "))
    elif ch == "3":
        h.view()
    else:
        break
