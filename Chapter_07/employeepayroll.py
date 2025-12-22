class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        hra = self.salary * 0.20
        da = self.salary * 0.10
        return self.salary + hra + da

e = Employee(101, "Riya", 30000)
print("Total Salary:", e.calculate_salary())
# Output: Total Salary: 39000.0
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        hra = self.salary * 0.20
        da = self.salary * 0.10
        return self.salary + hra + da
e = Employee(101, "Riya", 30000)
print("Total Salary:", e.calculate_salary())

