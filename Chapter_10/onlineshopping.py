cart = {}
shop_on = True

while shop_on:
    print("1.Add Item 2.View Cart 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        item = input("Item: ")
        price = int(input("Price: "))
        cart[item] = price
    elif ch == "2":
        print(cart, "Total:", sum(cart.values()))
    elif ch == "3":
        shop_on = False
