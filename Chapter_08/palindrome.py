def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

text = input("Enter text: ")
print("Palindrome" if is_palindrome(text) else "Not Palindrome")
