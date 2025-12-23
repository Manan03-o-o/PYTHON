def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

text = input("Enter text: ")
print("Palindrome" if is_palindrome(text) else "Not Palindrome")
# This program checks if the given text is a palindrome.
# It ignores spaces, punctuation, and is case-insensitive.
# Example:
# Input: "
# A man, a plan, a canal: Panama"
# Output: "Palindrome"  
# Input: "Hello"
# Output: "Not Palindrome"
