cart = {}
shopping = True

while shopping:
    print("1.Add Item 2.View Bill 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        cart[input("Item: ")] = int(input("Price: "))
    elif ch == "2":
        print(cart)
        print("Total:", sum(cart.values()))
    elif ch == "3":
        shopping = False
