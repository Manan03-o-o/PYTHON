class Library:
    def __init__(self):
        self.books = {}
        self.issued = {}

    def add_book(self, name, qty):
        self.books[name] = self.books.get(name, 0) + qty

    def issue_book(self, book, user):
        if self.books.get(book, 0) > 0:
            self.books[book] -= 1
            self.issued[user] = book
            return True
        return False

    def return_book(self, user):
        if user in self.issued:
            book = self.issued.pop(user)
            self.books[book] += 1

lib = Library()

while True:
    print("\n1.Add\n2.Issue\n3.Return\n4.Status\n5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        lib.add_book(input("Book: "), int(input("Qty: ")))

    elif ch == "2":
        if not lib.issue_book(input("Book: "), input("User: ")):
            print("Not Available")

    elif ch == "3":
        lib.return_book(input("User: "))

    elif ch == "4":
        print("Books:", lib.books)
        print("Issued:", lib.issued)

    else:
        break
