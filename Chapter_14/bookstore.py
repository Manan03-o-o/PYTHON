class BookStore:
    def __init__(self):
        self.books = {"Python":500, "Java":600}
        self.cart = {}

    def buy(self, book):
        if book in self.books:
            self.cart[book] = self.books[book]

    def bill(self):
        print(self.cart)
        print("Total:", sum(self.cart.values()))

store = BookStore()

while True:
    print("\n1.Buy 2.Bill 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        store.buy(input("Book: "))
    elif ch == "2":
        store.bill()
    else:
        break
