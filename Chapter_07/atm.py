class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_pin(self):
        p = input("Enter PIN: ")
        return p == self.pin

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    def deposit(self, amt):
        self.balance += amt
        print("Deposit Successful")

    def show_balance(self):
        print("Balance:", self.balance)

atm = ATM("1234", 5000)

if atm.check_pin():
    while True:
        print("1.Withdraw 2.Deposit 3.Balance 4.Exit")
        ch = input("Choice: ")
        if ch == "1":
            atm.withdraw(int(input("Amount: ")))
        elif ch == "2":
            atm.deposit(int(input("Amount: ")))
        elif ch == "3":
            atm.show_balance()
        else:
            break
else:
    print("Wrong PIN")
class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_pin(self):
        p = input("Enter PIN: ")
        return p == self.pin

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    def deposit(self, amt):
        self.balance += amt
        print("Deposit Successful")

    def show_balance(self):
        print("Balance:", self.balance)
