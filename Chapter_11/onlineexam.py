questions = {
    "2+2?":"4",
    "Capital of India?":"Delhi"
}

score = 0
for q,a in questions.items():
    if input(q+" ") == a:
        score += 1

print("Your score is:", score)



# This is a simple online exam program that asks two questions and calculates the score based on correct answers.
# The questions and their correct answers are stored in a dictionary.
# The user is prompted to answer each question, and the score is incremented for each correct answer.
# Finally, the total score is printed out.
# You can add more questions to the 'questions' dictionary to expand the exam.
# Note: This code does not include error handling or input validation for simplicity.
