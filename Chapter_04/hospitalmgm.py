patients = []

while True:
    print("\n1.Add Patient\n2.Search Patient\n3.View All\n4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        name = input("Name: ")
        age = int(input("Age: "))
        disease = input("Disease: ")
        patients.append({"name": name, "age": age, "disease": disease})

    elif ch == 2:
        n = input("Search name: ")
        for p in patients:
            if p["name"] == n:
                print("Found:", p)
                break
        else:
            print("Not Found")

    elif ch == 3:
        for p in patients:
            print(p)

    else:
        break
