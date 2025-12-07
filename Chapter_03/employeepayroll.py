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
