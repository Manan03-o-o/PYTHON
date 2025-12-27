stack = []

while True:
    print("1.Push 2.Pop 3.Peek 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        stack.append(input("Enter element: "))
    elif ch == "2":
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack Empty")
    elif ch == "3":
        print("Top:", stack[-1] if stack else "Empty")
    else:
        break
