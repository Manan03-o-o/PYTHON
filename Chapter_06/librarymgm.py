class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book Issued")
        else:
            print("Book Not Available")

    def display(self):
        print("Available Books:")
        for b in self.books:
            print(b)

lib = Library()
while True:
    print("1.Add 2.Issue 3.Display 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        lib.add_book(input("Book Name: "))
    elif ch == "2":
        lib.issue_book(input("Book Name: "))
    elif ch == "3":
        lib.display()
    else:
        break
