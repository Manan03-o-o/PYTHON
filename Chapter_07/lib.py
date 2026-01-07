books = {}
issued = {}
run = True

while run:
    print("1.Add Book 2.Issue 3.Return 4.Status 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        b = input("Book: ")
        books[b] = books.get(b, 0) + int(input("Qty: "))

    elif ch == "2":
        b = input("Book: ")
        u = input("User: ")
        if books.get(b, 0) > 0:
            books[b] -= 1
            issued[u] = b

    elif ch == "3":
        u = input("User: ")
        if u in issued:
            books[issued[u]] += 1
            del issued[u]

    elif ch == "4":
        print("Books:", books)
        print("Issued:", issued)

    elif ch == "5":
        run = False
