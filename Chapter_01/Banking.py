balance = 1000

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = int(input("Choice: "))

    if choice == 1:
        amt = int(input("Deposit amount: "))
        balance += amt
    elif choice == 2:
        amt = int(input("Withdraw amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient funds!")
    elif choice == 3:
        print("Balance =", balance)
    else:
        break
