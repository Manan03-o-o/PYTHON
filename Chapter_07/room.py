rooms = {101:"Empty", 102:"Empty", 103:"Empty"}
flag = True

while flag:
    print("1.Book 2.Checkout 3.Status 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        r = int(input("Room: "))
        if rooms.get(r) == "Empty":
            rooms[r] = input("Guest Name: ")

    elif ch == "2":
        r = int(input("Room: "))
        rooms[r] = "Empty"

    elif ch == "3":
        print(rooms)

    elif ch == "4":
        flag = False
    else:
        print("Invalid Choice")

print("Exiting...")


#This is a simple room booking system that allows booking rooms, checking out, viewing room status, and exiting the program.

