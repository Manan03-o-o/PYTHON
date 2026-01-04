students = {}

while True:
    print("\n1.Add Marks 2.Analyze 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        students[input("Name: ")] = list(map(int, input("Marks: ").split()))
    elif ch == "2":
        for s,m in students.items():
            avg = sum(m)/len(m)
            print(s, "Average:", avg)
    else:
        break
