n = int(input("Enter number of students: "))

students = {}

for _ in range(n):
    name = input("Name: ")
    m1 = int(input("Math: "))
    m2 = int(input("Science: "))
    m3 = int(input("English: "))
    avg = (m1 + m2 + m3) / 3
    students[name] = avg

for name, avg in students.items():
    print(f"{name} -> Average: {avg}")

top_student = max(students, key=students.get)
print(f"Top student: {top_student} with average {students[top_student]}")
# Student Grade Calculator
# This program calculates the average grade of students and identifies the top student.
# It prompts the user to enter the number of students and their respective grades in three subjects.
# The program calculates the average grade for each student and stores it in a dictionary.
# Finally, it prints the average grades and the name of the student with the highest average.


