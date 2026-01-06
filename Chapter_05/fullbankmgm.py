accounts = {
    "101": {"name": "Manan", "balance": 5000},
    "102": {"name": "Riya", "balance": 7000},
    "103": {"name": "Amit", "balance": 3000}
}

def deposit():
    acc = input("Account number: ")
    amt = int(input("Amount: "))
    if acc in accounts:
        accounts[acc]["balance"] += amt
        print("Deposited")
    else:
        print("Invalid account")

def withdraw():
    acc = input("Account number: ")
    amt = int(input("Amount: "))
    if acc in accounts and accounts[acc]["balance"] >= amt:
        accounts[acc]["balance"] -= amt
        print("Withdrawn")
    else:
        print("Insufficient funds or invalid account")

def show():
    acc = input("Account number: ")
    print(accounts.get(acc, "No account"))

while True:
    print("\n1.Deposit 2.Withdraw 3.Show 4.Exit")
    c = int(input("Choice: "))
    if c == 1: deposit()
    elif c == 2: withdraw()
    elif c == 3: show()
    else: break
