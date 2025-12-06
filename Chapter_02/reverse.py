sentence = input("Enter sentence: ")

words = sentence.split()
rev = " ".join(words[::-1])

print("Reversed:", rev)
print("Original:", sentence)
print("Original id:", id(sentence))
print("Reversed id:", id(rev))

print
("Are they the same object?", sentence is rev)
print("Are they equal?", sentence == rev)

print("Original length:", len(sentence))
