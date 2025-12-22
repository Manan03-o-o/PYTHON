import random
import string

db = {}

def shorten(url):
    key = ''.join(random.choices(string.ascii_letters, k=6))
    db[key] = url
    return key

def expand(key):
    return db.get(key, "Not Found")

short = shorten("https://google.com")
print("Short URL:", short)
print("Original:", expand(short))
