chat=[]

while True:
    print("1.Send 2.View 3.Exit")
    c=input("Choice: ")
    if c=="1":
        chat.append(input("Msg: "))
    elif c=="2":
        for m in chat: print(m)
    else: break
