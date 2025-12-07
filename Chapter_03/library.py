books = ["HarryPotter", "Avengers", "Python", "DataScience"]

borrowed = []

while True:
    print("\n1.Show Books\n2.Borrow\n3.Return\n4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        print("Available:", books)
        print("Borrowed:", borrowed)

    elif ch == 2:
        b = input("Book name: ")
        if b in books:
            books.remove(b)
            borrowed.append(b)
            print("Borrowed!")
        else:
            print("Not available!")

    elif ch == 3:
        b = input("Return book: ")
        if b in borrowed:
            borrowed.remove(b)
            books.append(b)
            print("Returned!")
        else:
            print("You don't have that book!")

    else:
        break

print("Thank you for using the library!")


