menu = {"Burger":120, "Pizza":250, "Pasta":180}
cart = {}

while True:
    print("\n1.Menu 2.Add Item 3.Bill 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        for i,p in menu.items():
            print(i, p)
    elif ch == "2":
        item = input("Item: ")
        if item in menu:
            cart[item] = cart.get(item, 0) + menu[item]
    elif ch == "3":
        print(cart)
        print("Total:", sum(cart.values()))
    else:
        break
