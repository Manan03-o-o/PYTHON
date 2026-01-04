orders = {}

while True:
    print("\n1.Place Order 2.Update Status 3.View 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        orders[input("Order ID: ")] = "Placed"
    elif ch == "2":
        oid = input("Order ID: ")
        if oid in orders:
            orders[oid] = input("New Status: ")
    elif ch == "3":
        print(orders)
    else:
        break
