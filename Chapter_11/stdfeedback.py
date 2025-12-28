feedback = {}

while True:
    print("\n1.Add Feedback 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        feedback[input("Name: ")] = input("Feedback: ")
    elif ch == "2":
        print(feedback)
    else:
        break
