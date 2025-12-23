students = {
    "Amit": [80, 70, 90],
    "Riya": [85, 88, 92]
}

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(name, "Average:", avg)
