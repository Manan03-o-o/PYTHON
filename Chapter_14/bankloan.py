class LoanSystem:
    def __init__(self):
        self.loans = {}

    def apply(self, name, amt):
        self.loans[name] = {"amount": amt, "status": "Pending"}

    def approve(self, name):
        if name in self.loans:
            self.loans[name]["status"] = "Approved"

    def view(self):
        print(self.loans)

l = LoanSystem()

while True:
    print("\n1.Apply 2.Approve 3.View 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        l.apply(input("Name: "), int(input("Amount: ")))
    elif ch == "2":
        l.approve(input("Name: "))
    elif ch == "3":
        l.view()
    else:
        break
