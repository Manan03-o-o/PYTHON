dictionary = {}

for _ in range(3):
    word = input("Word: ")
    meaning = input("Meaning: ")
    synonym = input("Synonym: ")
    dictionary[word] = {"meaning": meaning, "synonym": synonym}

search = input("Search word: ")

if search in dictionary:
    print("Meaning:", dictionary[search]["meaning"])
    print("Synonym:", dictionary[search]["synonym"])
else:
    print("Not found!")
