class University:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, roll, name):
        self.students[roll] = {"name": name, "courses": []}

    def add_course(self, code, name):
        self.courses[code] = name

    def enroll(self, roll, code):
        if roll in self.students and code in self.courses:
            self.students[roll]["courses"].append(code)

    def view(self):
        print("Students:")
        for r, d in self.students.items():
            print(r, d)

u = University()

while True:
    print("\n1.Add Student 2.Add Course 3.Enroll 4.View 5.Exit")
    ch = input("Choice: ")
    if ch == "1":
        u.add_student(input("Roll: "), input("Name: "))
    elif ch == "2":
        u.add_course(input("Code: "), input("Course Name: "))
    elif ch == "3":
        u.enroll(input("Roll: "), input("Course Code: "))
    elif ch == "4":
        u.view()
    else:
        break
