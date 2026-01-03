items = {}
sales = []

while True:
    print("\n1.Add Item 2.Sell 3.Report 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        items[input("Item: ")] = int(input("Price: "))
    elif ch == "2":
        i = input("Item: ")
        if i in items:
            sales.append(items[i])
    elif ch == "3":
        print("Sales:", sales)
        print("Total:", sum(sales))
    else:
        break
