employees = {}
loop = True

while loop:
    print("1.Add Emp 2.Mark Days 3.Salary 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        employees[input("Name: ")] = {"days": 0}

    elif ch == "2":
        n = input("Name: ")
        if n in employees:
            employees[n]["days"] += 1

    elif ch == "3":
        for e in employees:
            print(e, employees[e]["days"] * 1000)

    elif ch == "4":
        loop = False
