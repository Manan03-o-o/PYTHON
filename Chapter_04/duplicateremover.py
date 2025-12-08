sentence = input("Enter sentence: ").split()

unique = []
for w in sentence:
    if w not in unique:
        unique.append(w)

print(" ".join(unique))
# This program removes duplicate words from a sentence while preserving the order of first occurrences.
# Example:
# Input: "
# Enter sentence: this is a test this is only a test

# Output:
# this is a test only
# Output: "this is a test only"

