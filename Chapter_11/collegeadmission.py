class Admission:
    def __init__(self):
        self.students = {}

    def apply(self, name, marks):
        self.students[name] = marks

    def merit_list(self):
        for s in sorted(self.students, key=self.students.get, reverse=True):
            print(s, self.students[s])

adm = Admission()

while True:
    print("\n1.Apply 2.Merit List 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        adm.apply(input("Name: "), int(input("Marks: ")))
    elif ch == "2":
        adm.merit_list()
    else:
        break
