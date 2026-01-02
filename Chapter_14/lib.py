books = ["Python Basics", "Data Structures", "AI Intro"]

while True:
    print("\n1.Search 2.View All 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        k = input("Keyword: ")
        for b in books:
            if k.lower() in b.lower():
                print(b)
    elif ch == "2":
        print(books)
    else:
        break
