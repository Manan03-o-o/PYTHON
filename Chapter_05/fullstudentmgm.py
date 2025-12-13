students = {}

def add_student():
    roll = input("Roll: ")
    name = input("Name: ")
    marks = int(input("Marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added.")

def update_student():
    roll = input("Roll to update: ")
    if roll in students:
        name = input("New name: ")
        marks = int(input("New marks: "))
        students[roll] = {"name": name, "marks": marks}
        print("Updated.")
    else:
        print("Roll not found.")

def delete_student():
    roll = input("Roll to delete: ")
    if roll in students:
        del students[roll]
        print("Deleted.")
    else:
        print("Roll not found.")

def search_student():
    roll = input("Roll: ")
    print(students.get(roll, "Student not found."))

def display_all():
    for roll, info in students.items():
        print(roll, "->", info)

while True:
    print("\n1.Add 2.Update 3.Delete 4.Search 5.Display 6.Exit")
    ch = int(input("Choice: "))
    if ch == 1: add_student()
    elif ch == 2: update_student()
    elif ch == 3: delete_student()
    elif ch == 4: search_student()
    elif ch == 5: display_all()
    else: break
