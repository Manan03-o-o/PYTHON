attendance = {}

n = int(input("Number of employees: "))

for _ in range(n):
    name = input("Name: ")
    days = int(input("Days present: "))
    attendance[name] = days

for name, days in attendance.items():
    print(name, "present", days, "days")
