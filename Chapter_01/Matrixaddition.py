A = []
B = []

print("Enter Matrix A:")
for _ in range(3):
    A.append(list(map(int, input().split())))

print("Enter Matrix B:")
for _ in range(3):
    B.append(list(map(int, input().split())))

C = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]

print("Result:")
for row in C:
    print(*row)
