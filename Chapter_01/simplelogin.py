users = {"admin": "1234", "user": "pass"}

u = input("Username: ")
p = input("Password: ")

if u in users and users[u] == p:
    print("Login Successful!")
else:
    print("Invalid credentials!")
