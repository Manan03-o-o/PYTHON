import shutil

while True:
    print("\n1.Backup 2.Restore 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        shutil.copy("data.txt", "backup.txt")
        print("Backup Done")
    elif ch == "2":
        shutil.copy("backup.txt", "data.txt")
        print("Restored")
    else:
        break
