def write_entry(text):
    with open("diary.txt", "a") as f:
        f.write(text + "\n")

def read_diary():
    with open("diary.txt") as f:
        print(f.read())

while True:
    print("\n1.Write 2.Read 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        write_entry(input("Entry: "))
    elif ch == "2":
        read_diary()
    else:
        break
