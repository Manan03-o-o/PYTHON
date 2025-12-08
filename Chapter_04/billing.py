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
