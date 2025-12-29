class Loan:
    def __init__(self):
        self.applications = {}

    def apply(self, name, amount):
        self.applications[name] = amount

    def approve(self):
        for k,v in self.applications.items():
            print(k, "Loan Approved:", v)

loan = Loan()

while True:
    print("\n1.Apply 2.Approve 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        loan.apply(input("Name: "), int(input("Amount: ")))
    elif ch == "2":
        loan.approve()
    else:
        break

  