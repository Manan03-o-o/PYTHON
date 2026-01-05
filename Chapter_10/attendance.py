attendance = {}
go = True

while go:
    print("1.Mark Present 2.View 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        attendance[input("Name: ")] = "Present"
    elif ch == "2":
        print(attendance)
    elif ch == "3":
        go = False
