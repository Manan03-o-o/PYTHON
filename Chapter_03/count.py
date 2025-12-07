with open("sample.txt", "r") as f:
    text = f.read()

lines = text.count("\n") + 1
words = len(text.split())
chars = len(text)

print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
print(f"Lines: {lines}\nWords: {words}\nCharacters: {chars}")
print(f"Lines: {lines}\nWords: {words}\nCharacters: {chars}")
print("Lines: {}\nWords: {}\nCharacters: {}".format(lines, words, chars))
print("Lines: {0}\nWords: {1}\nCharacters: {2}".format(lines, words, chars))
print("Lines: {lines}\nWords: {words}\nCharacters: {chars}".format(lines=lines, words=words, chars=chars))
print(f"""Lines: {lines}
Words: {words}
Characters: {chars}""")
print("Lines:", lines, "Words:", words, "Characters:", chars)
print("Lines: {}\nWords: {}\nCharacters: {}".format(lines, words, chars))
