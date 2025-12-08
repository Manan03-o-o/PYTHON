accounts = {
    "manan": 2000,
    "raj": 1500,
    "tara": 3000
}

user = input("Enter username: ")

if user in accounts:
    while True:
        print("\n1.Deposit\n2.Withdraw\n3.Balance\n4.Exit")
        ch = int(input("Choice: "))

        if ch == 1:
            amt = int(input("Amount: "))
            accounts[user] += amt

        elif ch == 2:
            amt = int(input("Amount: "))
            if amt <= accounts[user]:
                accounts[user] -= amt
            else:
                print("Low balance!")

        elif ch == 3:
            print("Balance =", accounts[user])

        else:
            break
else:
    print("User not found!")
    # End of banking.py
    
