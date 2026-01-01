import json, os, getpass

DB = "users.json"
users = json.load(open(DB)) if os.path.exists(DB) else {}

def save(): json.dump(users, open(DB,"w"), indent=2)

def signup():
    u = input("Username: ")
    if u in users: return print("Exists")
    p = getpass.getpass("Password: ")
    users[u] = {"pass": p, "bio": ""}
    save()

def login():
    u = input("Username: ")
    p = getpass.getpass("Password: ")
    if users.get(u,{}).get("pass")==p:
        print("Logged in"); profile(u)
    else: print("Invalid")

def profile(u):
    while True:
        print("1.View 2.Edit Bio 3.Logout")
        ch=input("Choice: ")
        if ch=="1": print(users[u])
        elif ch=="2":
            users[u]["bio"]=input("Bio: "); save()
        else: break

while True:
    print("1.Signup 2.Login 3.Exit")
    c=input("Choice: ")
    if c=="1": signup()
    elif c=="2": login()
    else: break
