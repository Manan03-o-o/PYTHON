class Voting:
    def __init__(self):
        self.candidates = {"A":0, "B":0}
        self.voted = set()

    def vote(self, voter, choice):
        if voter in self.voted:
            print("Already Voted")
        elif choice in self.candidates:
            self.candidates[choice] += 1
            self.voted.add(voter)

    def result(self):
        print(self.candidates)

v = Voting()

while True:
    print("\n1.Vote 2.Result 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        v.vote(input("Voter ID: "), input("Candidate A/B: "))
    elif ch == "2":
        v.result()
    else:
        break
