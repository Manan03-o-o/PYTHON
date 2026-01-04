transactions = []

while True:
    print("\n1.Deposit 2.Withdraw 3.History 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        transactions.append(("Deposit", int(input("Amount: "))))
    elif ch == "2":
        transactions.append(("Withdraw", int(input("Amount: "))))
    elif ch == "3":
        for t in transactions:
            print(t)
    else:
        break
