balance = 0
active = True

while active:
    print("1.Deposit 2.Withdraw 3.Balance 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        balance += int(input("Amount: "))
    elif ch == "2":
        balance -= int(input("Amount: "))
    elif ch == "3":
        print("Balance:", balance)
    elif ch == "4":
        active = False
    else:
        print("Invalid choice")
        continue

print("Exiting...")

print("Final Balance:", balance)

    
