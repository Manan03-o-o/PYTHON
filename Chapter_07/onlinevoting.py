candidates = {"A": 0, "B": 0}
voted = set()

while True:
    voter = input("Voter ID (or exit): ")
    if voter == "exit":
        break
    if voter in voted:
        print("Already Voted")
        continue
    choice = input("Vote A or B: ")
    if choice in candidates:
        candidates[choice] += 1
        voted.add(voter)

print("Results:", candidates)
