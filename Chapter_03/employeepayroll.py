class Employee:
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

    def salary(self):
        hra = 0.2 * self.basic
        da = 0.1 * self.basic
        return self.basic + hra + da

emp = Employee("Manan", 30000)
print("Employee:", emp.name)
print("Total Salary:", emp.salary())

# Output:   
# Employee: Manan
# Total Salary: 3600000.0
# Employee Payroll System
# This program calculates the total salary of an employee
# including HRA and DA based on the basic salary provided.
# HRA is 20% of basic salary
# DA is 10% of basic salary 
