inventory = {"Pen":10, "Book":50}
bill = {}

while True:
    print("\n1.Add 2.Buy 3.Bill 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        inventory[input("Item: ")] = int(input("Price: "))
    elif ch == "2":
        item = input("Item: ")
        if item in inventory:
            bill[item] = inventory[item]
    elif ch == "3":
        print(bill, "Total:", sum(bill.values()))
    else:
        break
