attendance = {}

while True:
    print("\n1.Mark 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        attendance[input("Name: ")] = "Present"
    elif ch == "2":
        print(attendance)
    else:
        break
