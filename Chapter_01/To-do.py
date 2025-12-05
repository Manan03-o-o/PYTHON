todo = []

while True:
    print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
    ch = int(input())

    if ch == 1:
        task = input("Task: ")
        todo.append(task)

    elif ch == 2:
        task = input("Task to remove: ")
        if task in todo:
            todo.remove(task)
        else:
            print("Task not found!")

    elif ch == 3:
        for t in todo:
            print("-", t)

    else:
        break
