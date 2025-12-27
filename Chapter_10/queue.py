queue = []

while True:
    print("1.Enqueue 2.Dequeue 3.Display 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        queue.append(input("Enter element: "))
    elif ch == "2":
        if queue:
            print("Removed:", queue.pop(0))
        else:
            print("Queue Empty")
    elif ch == "3":
        print(queue)
    else:
        break
    
