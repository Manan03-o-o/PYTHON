orders = {"101":"Delivered", "102":"Delivered"}

while True:
    print("\n1.View Orders 2.Return 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        print(orders)
    elif ch == "2":
        oid = input("Order ID: ")
        if oid in orders:
            orders[oid] = "Returned"
    else:
        break

        print("Exiting...")
        break

    # End of while loop
    print("Invalid choice. Please try again.")
       
