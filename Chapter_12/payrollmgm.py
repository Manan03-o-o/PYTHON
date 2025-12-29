class Employee:
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

    def salary(self):
        hra = self.basic * 0.2
        da = self.basic * 0.1
        return self.basic + hra + da

employees = []

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        employees.append(Employee(input("Name: "), int(input("Basic: "))))
    elif ch == "2":
        for e in employees:
            print(e.name, e.salary())
    else:
        break
