students = []

while True:
    print("\n1.Add Student\n2.View All\n3.Search\n4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        name = input("Name: ")
        roll = input("Roll: ")
        marks = int(input("Marks: "))
        students.append({"name": name, "roll": roll, "marks": marks})

    elif ch == 2:
        for s in students:
            print(s)

    elif ch == 3:
        r = input("Search Roll: ")
        for s in students:
            if s["roll"] == r:
                print("Found:", s)
                break
        else:
            print("Not Found")

    else:
        break
