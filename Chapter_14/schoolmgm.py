class School:
    def __init__(self):
        self.students = {}
        self.teachers = {}

    def add_student(self, roll, name, cls):
        self.students[roll] = {"name": name, "class": cls}

    def add_teacher(self, tid, name, subject):
        self.teachers[tid] = {"name": name, "subject": subject}

    def view(self):
        print("Students:", self.students)
        print("Teachers:", self.teachers)

s = School()

while True:
    print("\n1.Add Student 2.Add Teacher 3.View 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        s.add_student(input("Roll: "), input("Name: "), input("Class: "))
    elif ch == "2":
        s.add_teacher(input("ID: "), input("Name: "), input("Subject: "))
    elif ch == "3":
        s.view()
    elif ch == "4":
        break
    else:
        print("Invalid Choice")




            