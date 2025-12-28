feedback = {}

while True:
    print("\n1.Add Feedback 2.View 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        feedback[input("Name: ")] = input("Feedback: ")
    elif ch == "2":
        print(feedback)
    else:
        break

# This code allows users to add feedback associated with their names and view all feedback.
def add_feedback(name, comment):
    feedback[name] = comment
def view_feedback():
    return feedback
# Example usage:
# add_feedback("Alice", "Great service!")
# print(view_feedback())
# This code allows users to add feedback associated with their names and view all feedback.



