employees = {}

while True:
    print("\n1.Add Emp 2.Mark Present 3.Salary 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        employees[input("Name: ")] = {"days":0, "salary":0}
    elif ch == "2":
        n = input("Name: ")
        if n in employees:
            employees[n]["days"] += 1
    elif ch == "3":
        for e in employees:
            employees[e]["salary"] = employees[e]["days"] * 1000
            print(e, employees[e]["salary"])
    else:
        break

# End of payroll.py
# Payroll Management System
# Each employee is paid 1000 per day of attendance
# Employees are stored in a dictionary with their attendance and salary details
# User can add employees, mark attendance, and calculate salaries
# Simple command-line interface for interaction
    
