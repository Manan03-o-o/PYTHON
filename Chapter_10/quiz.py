questions = {"2+2":"4", "Capital of India":"Delhi"}
score = 0
keys = list(questions.keys())
i = 0

while i < len(keys):
    ans = input(keys[i] + ": ")
    if ans.lower() == questions[keys[i]].lower():
        score += 1
    i += 1

print("Score:", score)
