votes = {}

n = int(input("How many votes? "))

for _ in range(n):
    candidate = input("Vote for: ")
    votes[candidate] = votes.get(candidate, 0) + 1

print("\n--- Results ---")
for c, v in votes.items():
    print(c, ":", v)
# Voting System
# This program collects votes for candidates and displays the total votes for each candidate.
# It uses a dictionary to store candidate names as keys and their vote counts as values.

