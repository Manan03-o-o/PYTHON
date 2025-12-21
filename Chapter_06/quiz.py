questions = {
    "Capital of India?": "Delhi",
    "2 + 2 = ?": "4",
    "Python is ___ language": "interpreted"
}

score = 0
for q, a in questions.items():
    ans = input(q + " ")
    if ans.lower() == a.lower():
        score += 1

print("Score:", score, "/", len(questions))
