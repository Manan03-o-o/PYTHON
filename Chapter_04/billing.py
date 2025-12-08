menu = {"pizza": 150, "burger": 80, "pasta": 120, "coffee": 50}
bill = 0

while True:
    print("\nMenu:", menu)
    item = input("Order item (or 'exit'): ")

    if item == "exit":
        break
    elif item in menu:
        qty = int(input("Quantity: "))
        bill += menu[item] * qty
    else:
        print("Item not available")

print("Total bill =", bill)
# This code allows users to order items from a menu and calculates the total bill.
# Users can order multiple items until they choose to exit.
# The menu is represented as a dictionary with item names as keys and prices as values.
# The total bill is updated based on the items ordered and their quantities.
# If an item is not available in the menu, an error message is displayed.

