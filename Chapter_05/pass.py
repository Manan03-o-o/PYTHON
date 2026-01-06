correct = "python"
attempts = 3

while attempts > 0:
    pwd = input("Enter password: ")
    if pwd == correct:
        print("Access Granted")
        attempts = 0
    else:
        attempts -= 1
        print("Attempts left:", attempts)
        if attempts == 0:
            print("Access Denied")
        else:
            print("Incorrect password, try again.")
            
