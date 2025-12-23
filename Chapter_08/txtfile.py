from collections import Counter

with open("sample.txt", "r") as f:
    words = f.read().split()

count = Counter(words)

for w, c in count.items():
    print(w, ":", c)
