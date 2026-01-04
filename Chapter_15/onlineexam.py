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
