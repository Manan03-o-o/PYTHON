from collections import Counter

text = input("Enter text: ")
words = text.split()

freq = Counter(words)

for w, c in freq.items():
    print(w, ":", c)
# This code counts the frequency of each word in the input text and prints the results.
# Example usage:
# Input: "hello world hello"
# Output:
# hello : 2
# world : 1
# You can run this code in a Python environment to see how it works.

