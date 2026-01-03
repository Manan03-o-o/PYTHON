fees = {}

while True:
    print("\n1.Pay Fee 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        fees[input("Name: ")] = int(input("Amount: "))
    elif ch == "2":
        print(fees)
    else:
        break
    
    
    # Sample Interaction:
    # 1.Pay Fee 2.View 3.Exit
    # Choice: 1
    # Name: Alice
    # Amount: 1000
    #
    # 1.Pay Fee 2.View 3.Exit
    # Choice: 1
    # Name: Bob
    # Amount: 1500
    # 1.Pay Fee 2.View 3.Exit
    # Choice: 2
    # {'Alice': 1000, 'Bob': 1500}
    