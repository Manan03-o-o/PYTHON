import os

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.roll},{self.name},{self.marks}"

FILE = "students.txt"

def add_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    marks = input("Marks: ")
    s = Student(roll, name, marks)
    with open(FILE, "a") as f:
        f.write(str(s) + "\n")

def view_students():
    if not os.path.exists(FILE):
        print("No records found")
        return
    with open(FILE) as f:
        for line in f:
            r, n, m = line.strip().split(",")
            print(f"Roll:{r} Name:{n} Marks:{m}")

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        break
