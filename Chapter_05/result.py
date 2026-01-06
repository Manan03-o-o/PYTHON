students = {}
run = True

while run:
    print("1.Add Marks 2.View Results 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        students[input("Name: ")] = int(input("Marks: "))
    elif ch == "2":
        for s,m in students.items():
            print(s, "Pass" if m>=40 else "Fail")
    elif ch == "3":
        run = False
