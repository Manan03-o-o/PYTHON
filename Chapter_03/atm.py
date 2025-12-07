pin = "1234"
balance = 2000
attempts = 0

while attempts < 3:
    p = input("Enter PIN: ")
    
    if p == pin:
        print("Login Successful!")
        while True:
            print("\n1.Deposit\n2.Withdraw\n3.Balance\n4.Exit")
            c = int(input())
            if c == 1:
                amt = int(input("Amount: "))
                balance += amt
            elif c == 2:
                amt = int(input("Amount: "))
                if amt <= balance:
                    balance -= amt
                else:
                    print("Not enough balance!")
            elif c == 3:
                print("Balance:", balance)
            else:
                exit()
    else:
        attempts += 1
        print("Wrong PIN!")

print("Your card is blocked!")
