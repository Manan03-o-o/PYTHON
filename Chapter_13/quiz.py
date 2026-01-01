import time

qs=[("2+3","5"),("Capital of India","Delhi")]
score=0
for q,a in qs:
    print(q)
    start=time.time()
    ans=input("Ans: ")
    if time.time()-start<=10 and ans.lower()==a.lower():
        score+=1
print("Score:",score)
print("Quiz Over!")
print("You scored",score,"out of",len(qs))
with open("quiz_score.txt","a") as f:
    f.write(f"Score: {score} out of {len(qs)}\n")
print("Your score has been recorded in quiz_score.txt")

    
