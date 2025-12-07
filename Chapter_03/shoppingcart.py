cart = {}
while True:
    print("\n1.Add item\n2.View cart\n3.Total bill\n4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        item = input("Item name: ")
        price = int(input("Price: "))
        qty = int(input("Quantity: "))
        cart[item] = cart.get(item, 0) + price * qty

    elif ch == 2:
        for i, cost in cart.items():
            print(i, "=", cost)

    elif ch == 3:
        print("Total Bill =", sum(cart.values()))

    else:
        break
