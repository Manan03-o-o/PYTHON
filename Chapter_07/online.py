products = {"Laptop":50000, "Phone":20000}
cart = {}
shop = True

while shop:
    print("1.View 2.Add 3.Bill 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        print(products)

    elif ch == "2":
        p = input("Product: ")
        if p in products:
            cart[p] = products[p]

    elif ch == "3":
        print(cart)
        print("Total:", sum(cart.values()))

    elif ch == "4":
        shop = False
