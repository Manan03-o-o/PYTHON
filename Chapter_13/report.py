import os

def search(root, word):
    hits=[]
    for r,_,fs in os.walk(root):
        for f in fs:
            p=os.path.join(r,f)
            try:
                if word in open(p,errors="ignore").read():
                    hits.append(p)
            except: pass
    open("report.txt","w").write("\n".join(hits))

search(".", input("Word: "))
print("Report generated")
# This script searches for a specified word in all files within the current directory and its subdirectories. It generates a report of file paths containing the word and saves it to 'report.txt'.
# Usage:
# 1. Run the script.
# 2. Input the word you want to search for when prompted.
# 3. Check 'report.txt' for the list of files containing the word.

# Example:
# If you run the script and input "example", it will search all files for the word
# "example" and list the paths of those files in 'report.txt'.
# Note: The script ignores files that cannot be opened due to permission issues or other errors.

