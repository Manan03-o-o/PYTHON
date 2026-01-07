students = {}
courses = {}
running = True

while running:
    print("1.Add Student 2.Add Course 3.Enroll 4.View 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        r = input("Roll: ")
        students[r] = {"name": input("Name: "), "courses": []}

    elif ch == "2":
        c = input("Course Code: ")
        courses[c] = input("Course Name: ")

    elif ch == "3":
        r = input("Roll: ")
        c = input("Course Code: ")
        if r in students and c in courses:
            students[r]["courses"].append(c)

    elif ch == "4":
        print(students)

    elif ch == "5":
        running = False
    else:
        print("Invalid Choice")

        # End of the program
        # End of the program
print("Exiting...")


#this is a simple student management system that allows adding students and courses, enrolling students in courses, and viewing the current data.

