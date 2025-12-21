FILE = "todo.txt"

def add_task(task):
    with open(FILE, "a") as f:
        f.write(task + "\n")

def view_tasks():
    with open(FILE) as f:
        for i, t in enumerate(f, 1):
            print(i, t.strip())

while True:
    print("1.Add 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        add_task(input("Task: "))
    elif ch == "2":
        view_tasks()
    else:
        break
