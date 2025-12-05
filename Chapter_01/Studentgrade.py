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

