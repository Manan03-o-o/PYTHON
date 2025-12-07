tasks = []

while True:
    print("\n1.Add\n2.View\n3.Save to File\n4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        task = input("Task: ")
        tasks.append(task)

    elif ch == 2:
        for t in tasks:
            print("-", t)

    elif ch == 3:
        with open("tasks.txt", "w") as f:
            for t in tasks:
                f.write(t + "\n")
        print("Saved!")

    else:
        break
