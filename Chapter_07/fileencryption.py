def encrypt(text, key):
    result = ""
    for c in text:
        result += chr(ord(c) + key)
    return result

def decrypt(text, key):
    result = ""
    for c in text:
        result += chr(ord(c) - key)
    return result

msg = input("Message: ")
key = 3

enc = encrypt(msg, key)
print("Encrypted:", enc)
print("Decrypted:", decrypt(enc, key))
