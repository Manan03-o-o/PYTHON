password = "admin"
attempts = 3

while attempts > 0:
    p = input("Enter password: ")
    if p == password:
        print("Login Success")
        attempts = 0
    else:
        attempts -= 1
        print("Attempts left:", attempts)
        if attempts == 0:
            print("Login Failed")
            break
        
print("Exiting...")