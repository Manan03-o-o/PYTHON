users = {
    "admin": {"pass":"123", "role":"ADMIN"},
    "user": {"pass":"111", "role":"USER"}
}

u = input("Username: ")
p = input("Password: ")

if u in users and users[u]["pass"] == p:
    print("Role:", users[u]["role"])
else:
    print("Invalid Login")

# Example usage:
# Username: admin
# Password: 123
# Role: ADMIN
# Username: user
# Password: 111
# Role: USER
# Username: guest
# Password: 000
# Invalid Login


