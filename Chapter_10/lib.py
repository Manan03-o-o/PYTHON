books = {"Python":2, "Java":1}
run = True

while run:
    print("1.Issue 2.Return 3.View 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        b = input("Book: ")
        if books.get(b,0) > 0:
            books[b] -= 1
    elif ch == "2":
        b = input("Book: ")
        books[b] = books.get(b,0) + 1
    elif ch == "3":
        print(books)
    elif ch == "4":
        run = False

