import getpass

users = {"admin": ("1234", "ADMIN"), "user": ("1111", "USER")}

def login():
    u = input("Username: ")
    p = getpass.getpass("Password: ")
    if u in users and users[u][0] == p:
        return users[u][1]
    return None

role = login()

if role == "ADMIN":
    print("Admin Panel")
elif role == "USER":
    print("User Panel")
else:
    print("Invalid Login")
