text = input("Enter text: ").lower().split()

freq = {}

for w in text:
    freq[w] = freq.get(w, 0) + 1

for w in sorted(freq):
    print(w, ":", freq[w])
