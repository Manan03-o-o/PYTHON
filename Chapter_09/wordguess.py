word = "python"
guessed = "_" * len(word)

while "_" in guessed:
    ch = input("Guess letter: ")
    guessed = ''.join(
        ch if word[i] == ch else guessed[i]
        for i in range(len(word))
    )
    print(guessed)

print("You Win!")
