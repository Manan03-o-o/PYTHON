inventory = {}

while True:
    print("\n1.Add/Update Item\n2.Show Inventory\n3.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        name = input("Item name: ")
        qty = int(input("Quantity: "))
        inventory[name] = inventory.get(name, 0) + qty

    elif ch == 2:
        for item, q in inventory.items():
            print(item, ":", q)

    else:
        break
