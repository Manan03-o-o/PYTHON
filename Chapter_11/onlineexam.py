questions = {
    "2+2?":"4",
    "Capital of India?":"Delhi"
}

score = 0
for q,a in questions.items():
    if input(q+" ") == a:
        score += 1

print("Score:", score)
