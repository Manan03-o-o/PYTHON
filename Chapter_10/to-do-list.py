todos = []
flag = True

while flag:
    print("1.Add 2.View 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        todos.append(input("Task: "))
    elif ch == "2":
        print(todos)
    elif ch == "3":
        flag = False
