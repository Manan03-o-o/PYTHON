def search_word(word):
    with open("data.txt") as f:
        for i, line in enumerate(f, 1):
            if word.lower() in line.lower():
                print(f"Found at line {i}: {line.strip()}")

search_word(input("Search: "))
