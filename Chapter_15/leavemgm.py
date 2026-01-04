employees = {}

while True:
    print("\n1.Add Emp 2.Apply Leave 3.View 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        employees[input("Name: ")] = 0
    elif ch == "2":
        n = input("Name: ")
        if n in employees:
            employees[n] += int(input("Days: "))
    elif ch == "3":
        print(employees)
    else:
        break
