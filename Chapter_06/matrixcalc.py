def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

print("Sum:", add(A, B))
def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("Difference:", subtract(A, B))
def multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
print("Product:", multiply(A, B))
def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print("Transpose:", transpose(A))
print("Transpose:", transpose(B))
def adjoint(A):
    transposed = transpose(A)
    adj = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            minor = [row[:j] + row[j+1:] for k, row in enumerate(transposed) if k != i]
            det = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
            adj[i][j] = ((-1) ** (i + j)) * det
    return adj
print("Adjoint A:", adjoint(A))
print("Adjoint B:", adjoint(B))
def inverse(A):
    det = determinant(A)
    if det == 0:
        return None
    
    adj = adjoint(A)
    inv = [[adj[i][j] / det for j in range(len(A))] for i in range(len(A))]
    return inv
def determinant(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]
print("Inverse A:", inverse(A))
print("Inverse B:", inverse(B))
def determinant(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]
print("Determinant A:", determinant(A))
print("Determinant B:", determinant(B))
def power(A, n):    
    result = A
    for _ in range(n - 1):
        result = multiply(result, A)
    return result
print("A^2:", power(A, 2))
print("B^2:", power(B, 2))
print("A^3:", power(A, 3))
print("B^3:", power(B, 3))
print("A^4:", power(A, 4))
print("B^4:", power(B, 4))


