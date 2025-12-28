menu = {"Burger":100, "Pizza":200}
order = {}

while True:
    print("\n1.Order 2.Bill 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        item = input("Item: ")
        if item in menu:
            order[item] = menu[item]
    elif ch == "2":
        print(order, "Total:", sum(order.values()))
    else:
        break

print("Thank you!")
# End of file
