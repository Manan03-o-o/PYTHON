class Course:
    def __init__(self):
        self.courses = {}
        self.enrolled = {}

    def add_course(self, name):
        self.courses[name] = []

    def enroll(self, course, student):
        if course in self.courses:
            self.courses[course].append(student)

    def show(self):
        print(self.courses)

c = Course()

while True:
    print("\n1.Add Course 2.Enroll 3.View 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        c.add_course(input("Course Name: "))
    elif ch == "2":
        c.enroll(input("Course: "), input("Student: "))
    elif ch == "3":
        c.show()
    else:
        break
