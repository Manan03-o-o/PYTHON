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
