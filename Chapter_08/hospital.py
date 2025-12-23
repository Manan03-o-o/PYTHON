class Patient:
    def __init__(self, pid, name, disease):
        self.pid = pid
        self.name = name
        self.disease = disease

patients = []

while True:
    print("1.Add Patient 2.View Patients 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        pid = input("ID: ")
        name = input("Name: ")
        disease = input("Disease: ")
        patients.append(Patient(pid, name, disease))
    elif ch == "2":
        for p in patients:
            print(p.pid, p.name, p.disease)
    else:
        break
