inventory = {}
flag = True

while flag:
    print("1.Add Item 2.Update Qty 3.View 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        inventory[input("Item: ")] = int(input("Qty: "))
    elif ch == "2":
        i = input("Item: ")
        if i in inventory:
            inventory[i] = int(input("New Qty: "))
    elif ch == "3":
        print(inventory)
    elif ch == "4":
        flag = False
