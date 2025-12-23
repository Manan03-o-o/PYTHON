students = {
    "Amit": [80, 70, 90],
    "Riya": [85, 88, 92]
}

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(name, "Average:", avg)
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(name, "Grade:", grade)
    print()  # Print a newline for better readability
# Adding a new student  
students["John"] = [75, 85, 80]
name = "John"
marks = students[name]
avg = sum(marks) / len(marks)
print(name, "Average:", avg)
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'
print(name, "Grade:", grade)
# Print a newline for better readability
