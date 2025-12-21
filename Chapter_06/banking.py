class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt

    def display(self):
        print(self.acc_no, self.name, self.balance)

acc = BankAccount("101", "Manan", 1000)

while True:
    print("1.Deposit 2.Withdraw 3.Display 4.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        acc.deposit(int(input("Amount: ")))
    elif ch == 2:
        acc.withdraw(int(input("Amount: ")))
    elif ch == 3:
        acc.display()
    else:
        break
