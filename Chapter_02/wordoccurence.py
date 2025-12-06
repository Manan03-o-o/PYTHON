text = input("Enter text: ").lower().split()

freq = {}

for w in text:
    freq[w] = freq.get(w, 0) + 1

for w in sorted(freq):
    print(w, ":", freq[w])
# This program counts the occurrences of each word in the input text
# and prints them in alphabetical order.    
# It converts the text to lowercase to ensure that the count is case-insensitive.
# The use of a dictionary allows for efficient counting of word occurrences.
# The sorted function is used to display the words in alphabetical order.
# Example:
# Input: "Hello world hello"
# Output:
# hello : 2
# world : 1

