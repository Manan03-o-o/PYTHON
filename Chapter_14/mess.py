menu = {"Rice":40, "Dal":30}
orders = {}

while True:
    print("\n1.Order 2.Bill 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        item = input("Item: ")
        if item in menu:
            orders[item] = menu[item]
    elif ch == "2":
        print("Orders:", orders)
        print("Total:", sum(orders.values()))
    else:
        break
    # End of loop
        
    
