employees = {}

while True:
    print("\n1.Add Emp 2.Mark Present 3.Salary 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        employees[input("Name: ")] = {"days":0, "salary":0}
    elif ch == "2":
        n = input("Name: ")
        if n in employees:
            employees[n]["days"] += 1
    elif ch == "3":
        for e in employees:
            employees[e]["salary"] = employees[e]["days"] * 1000
            print(e, employees[e]["salary"])
    else:
        break
