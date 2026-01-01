tasks=[]

def add():
    tasks.append({
        "title":input("Title: "),
        "prio":input("Priority(H/M/L): "),
        "done":False
    })

def update():
    for i,t in enumerate(tasks): print(i,t)
    i=int(input("Index: "))
    tasks[i]["done"]=True

while True:
    print("1.Add 2.Done 3.View 4.Exit")
    c=input("Choice: ")
    if c=="1": add()
    elif c=="2": update()
    elif c=="3":
        for t in tasks: print(t)
    else: break
