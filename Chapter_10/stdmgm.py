running = True
students = {}

while running:
    print("1.Add 2.View 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        roll = input("Roll: ")
        students[roll] = input("Name: ")
    elif ch == "2":
        print(students)
    elif ch == "3":
        running = False
    else:
        print("Invalid Choice")
        continue
print("Exiting...")

