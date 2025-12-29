class Employee:
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

    def salary(self):
        hra = self.basic * 0.2
        da = self.basic * 0.1
        return self.basic + hra + da

employees = []

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        employees.append(Employee(input("Name: "), int(input("Basic: "))))
    elif ch == "2":
        for e in employees:
            print(e.name, e.salary())
    else:
        break

# End of payrollmgm.py
# Payroll Management System
# This program allows adding employees and viewing their salaries.
# Each employee's salary is calculated based on basic pay, HRA, and DA.
# HRA is 20% of basic pay and DA is 10% of basic pay.
# The program runs in a loop until the user chooses to exit.

# Example Usage:
# 1. Add an employee with name "John" and basic pay 1000.
# 2. View the list of employees and their calculated salaries.
# 3. Exit the program.

