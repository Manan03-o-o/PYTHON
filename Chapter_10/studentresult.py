class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        p = self.percentage()
        if p >= 90: return "A"
        if p >= 75: return "B"
        if p >= 60: return "C"
        return "Fail"

students = {}

while True:
    print("\n1.Add Student\n2.View Result\n3.Topper\n4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        roll = input("Roll: ")
        name = input("Name: ")
        marks = list(map(int, input("Enter marks: ").split()))
        students[roll] = Student(roll, name, marks)

    elif ch == "2":
        roll = input("Roll: ")
        s = students.get(roll)
        if s:
            print(s.name, s.total(), s.percentage(), s.grade())

    elif ch == "3":
        topper = max(students.values(), key=lambda x: x.total())
        print("Topper:", topper.name)

    else:
        break
