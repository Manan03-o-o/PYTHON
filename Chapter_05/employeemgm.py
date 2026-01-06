employees = {}
running = True

while running:
    print("1.Add 2.View 3.Delete 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        eid = input("ID: ")
        employees[eid] = input("Name: ")
    elif ch == "2":
        print(employees)
    elif ch == "3":
        eid = input("ID to delete: ")
        if eid in employees:
            del employees[eid]
    elif ch == "4":
        running = False
    else:
        print("Invalid choice")
        continue

print("Exiting...")

