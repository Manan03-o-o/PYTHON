votes = {}

n = int(input("How many votes? "))

for _ in range(n):
    candidate = input("Vote for: ")
    votes[candidate] = votes.get(candidate, 0) + 1

print("\n--- Results ---")
for c, v in votes.items():
    print(c, ":", v)
