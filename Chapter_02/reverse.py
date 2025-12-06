sentence = input("Enter sentence: ")

words = sentence.split()
rev = " ".join(words[::-1])

print("Reversed:", rev)
