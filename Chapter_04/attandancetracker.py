attendance = {}

n = int(input("Number of employees: "))

for _ in range(n):
    name = input("Name: ")
    days = int(input("Days present: "))
    attendance[name] = days

for name, days in attendance.items():
    print(name, "present", days, "days")
total_days = sum(attendance.values())
print("Total days present for all employees:", total_days)

absent_days = n * 30 - total_days
print("Total absent days for all employees:", absent_days)

absent_report = {name: 30 - days for name, days in attendance.items()}
print("Absent days report:")
for name, days in absent_report.items():
    print(name, "absent", days, "days")

