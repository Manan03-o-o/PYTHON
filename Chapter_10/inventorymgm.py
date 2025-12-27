inventory = {}

while True:
    print("\n1.Add\n2.Sell\n3.View\n4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        item = input("Item: ")
        qty = int(input("Qty: "))
        inventory[item] = inventory.get(item, 0) + qty

    elif ch == "2":
        item = input("Item: ")
        qty = int(input("Qty: "))
        if inventory.get(item, 0) >= qty:
            inventory[item] -= qty

    elif ch == "3":
        print(inventory)

    else:
        break
