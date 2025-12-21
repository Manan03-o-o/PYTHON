users = {"admin": "1234"}

u = input("Username: ")
p = input("Password: ")

if users.get(u) == p:
    print("Login Success")
else:
    print("Invalid Credentials")
