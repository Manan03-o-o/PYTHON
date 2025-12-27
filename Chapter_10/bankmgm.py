import os
import datetime

FILE = "bank_data.txt"

class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt > self.balance:
            return False
        self.balance -= amt
        return True

def load_accounts():
    accounts = {}
    if os.path.exists(FILE):
        with open(FILE) as f:
            for line in f:
                acc, name, bal = line.strip().split(",")
                accounts[acc] = Account(acc, name, float(bal))
    return accounts

def save_accounts(accounts):
    with open(FILE, "w") as f:
        for acc in accounts.values():
            f.write(f"{acc.acc_no},{acc.name},{acc.balance}\n")

accounts = load_accounts()

while True:
    print("\n1.Create Account\n2.Deposit\n3.Withdraw\n4.View\n5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        acc = input("Account No: ")
        name = input("Name: ")
        bal = float(input("Initial Balance: "))
        accounts[acc] = Account(acc, name, bal)

    elif ch == "2":
        acc = input("Account No: ")
        amt = float(input("Amount: "))
        if acc in accounts:
            accounts[acc].deposit(amt)

    elif ch == "3":
        acc = input("Account No: ")
        amt = float(input("Amount: "))
        if acc in accounts:
            if not accounts[acc].withdraw(amt):
                print("Insufficient balance")

    elif ch == "4":
        for a in accounts.values():
            print(a.acc_no, a.name, a.balance)

    else:
        save_accounts(accounts)
        break
