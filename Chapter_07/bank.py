balance = 0
history = []
active = True

while active:
    print("1.Deposit 2.Withdraw 3.History 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        amt = int(input("Amount: "))
        balance += amt
        history.append(("Deposit", amt))

    elif ch == "2":
        amt = int(input("Amount: "))
        if amt <= balance:
            balance -= amt
            history.append(("Withdraw", amt))

    elif ch == "3":
        print("Balance:", balance)
        print("History:", history)

    elif ch == "4":
        active = False
    else:
        print("Invalid choice")
        
