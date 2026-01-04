questions = {
    "2+5": "7",
    "Capital of India": "Delhi",
    "5*6": "30"
}

score = 0
for q,a in questions.items():
    ans = input(q + " = ")
    if ans.strip().lower() == a.lower():
        score += 1

print("Final Score:", score, "/", len(questions))

# This code implements a simple online exam system where users answer predefined questions.
# It keeps track of the score based on correct answers and displays the final score at the end.

# The questions are stored in a dictionary with the question as the key and the answer as the value.
# The user's input is compared to the correct answer in a case-insensitive manner.

# Example interaction:
# 2+5 = 7
# Capital of India = Delhi
# 5*6 = 30
# Final Score: 3 / 3

