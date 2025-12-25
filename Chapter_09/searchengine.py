def search_word(word):
    with open("data.txt") as f:
        for i, line in enumerate(f, 1):
            if word.lower() in line.lower():
                print(f"Found at line {i}: {line.strip()}")

search_word(input("Search: "))


# This function searches for a word in a text file and prints the lines where it is found, along with line numbers.
# It performs a case-insensitive search.
# Usage: Call the function with the desired word to search for.
# Example: search_word("example")
def search_word(word):
    with open("data.txt") as f:
        for i, line in enumerate(f, 1):
            if word.lower() in line.lower():
                print(f"Found at line {i}: {line.strip()}")

search_word(input("Search: "))
def search_word(word):
    with open("data.txt") as f:
        for i, line in enumerate(f, 1):
            if word.lower() in line.lower():
                print(f"Found at line {i}: {line.strip()}")
search_word(input("Search: "))



