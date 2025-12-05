from collections import Counter

text = input("Enter text: ")
words = text.split()

freq = Counter(words)

for w, c in freq.items():
    print(w, ":", c)
