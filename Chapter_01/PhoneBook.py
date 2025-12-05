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
