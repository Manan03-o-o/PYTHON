fees = {}

while True:
    print("\n1.Pay Fee 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        fees[input("Name: ")] = int(input("Amount: "))
    elif ch == "2":
        print(fees)
    else:
        break
