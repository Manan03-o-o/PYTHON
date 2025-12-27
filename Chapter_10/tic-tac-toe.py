board = [" "] * 9

def display():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def win(ch):
    combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==ch for a,b,c in combos)

turn = "X"
for _ in range(9):
    display()
    pos = int(input(f"{turn} position: "))
    if board[pos] == " ":
        board[pos] = turn
        if win(turn):
            print(turn, "Wins")
            break
        turn = "O" if turn == "X" else "X"
