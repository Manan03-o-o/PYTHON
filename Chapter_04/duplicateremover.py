sentence = input("Enter sentence: ").split()

unique = []
for w in sentence:
    if w not in unique:
        unique.append(w)

print(" ".join(unique))
