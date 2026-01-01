courses={}
students={}

while True:
    print("1.Add Course 2.Add Student 3.Register 4.View 5.Exit")
    c=input("Choice: ")
    if c=="1": courses[input("Course: ")]=[]
    elif c=="2": students[input("Student: ")]=[]
    elif c=="3":
        s=input("Student: "); c1=input("Course: ")
        if s in students and c1 in courses:
            students[s].append(c1); courses[c1].append(s)
    elif c=="4": print(students, courses)
    else: break
