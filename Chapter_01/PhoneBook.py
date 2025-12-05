phonebook = {}

n = int(input("How many contacts? "))

for _ in range(n):
    name = input("Name: ")
    num = input("Number: ")
    phonebook[name] = num

search = input("Search name: ")

if search in phonebook:
    print("Number:", phonebook[search])
else:
    print("Not found!")
    
# Create a simple phonebook application that allows users to add contacts and search for them.
# The program should:
# 1. Allow users to add a contact by entering a name and phone number.
# 2. Store the contacts in a dictionary.
# 3. Allow users to search for a contact by name and display the corresponding phone number
#    or a "Not found!" message if the contact does not exist.
