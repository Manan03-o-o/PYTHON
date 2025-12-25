import datetime

FILE = "expenses.txt"

def add_expense(amount, category):
    with open(FILE, "a") as f:
        f.write(f"{datetime.date.today()},{amount},{category}\n")

def view_expenses():
    try:
        with open(FILE) as f:
            for line in f:
                date, amt, cat = line.strip().split(",")
                print(f"{date} | ₹{amt} | {cat}")
    except FileNotFoundError:
        print("No expenses yet")

while True:
    print("1.Add 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        add_expense(input("Amount: "), input("Category: "))
    else:
        view_expenses()
        break
