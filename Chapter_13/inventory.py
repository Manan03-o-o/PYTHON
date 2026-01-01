inventory={}
suppliers={}

while True:
    print("1.Add Item 2.Add Supplier 3.Link 4.View 5.Exit")
    c=input("Choice: ")
    if c=="1":
        inventory[input("Item: ")]=int(input("Qty: "))
    elif c=="2":
        suppliers[input("Supplier: ")]=[]
    elif c=="3":
        s=input("Supplier: "); i=input("Item: ")
        if s in suppliers and i in inventory: suppliers[s].append(i)
    elif c=="4":
        print(inventory); print(suppliers)
    else: break
