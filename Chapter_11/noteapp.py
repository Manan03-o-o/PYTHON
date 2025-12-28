def add_note(note):
    with open("notes.txt","a") as f:
        f.write(note+"\n")

def view_notes():
    with open("notes.txt") as f:
        print(f.read())

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        add_note(input("Note: "))
    elif ch == "2":
        view_notes()
    else:
        break
