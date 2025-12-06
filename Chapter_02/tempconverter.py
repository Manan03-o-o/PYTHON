while True:
    print("\n1.C to F\n2.F to C\n3.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        c = float(input("Celsius: "))
        print("Fahrenheit =", (c * 9/5) + 32)

    elif ch == 2:
        f = float(input("Fahrenheit: "))
        print("Celsius =", (f - 32) * 5/9)

    else:
        break
