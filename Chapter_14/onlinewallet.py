class Wallet:
    def __init__(self):
        self.balance = 0

    def add(self, amt):
        self.balance += amt

    def pay(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient Balance")

w = Wallet()

while True:
    print("\n1.Add Money 2.Pay 3.View 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        w.add(int(input("Amount: ")))
    elif ch == "2":
        w.pay(int(input("Amount: ")))
    elif ch == "3":
        print("Balance:", w.balance)
    else:
        break
