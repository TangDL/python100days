import sys
[M, K, N] = list(map(int, sys.stdin.readline().strip().split()))

A = []
B = []
for i in range(M):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    A.append(temp)
for i in range(K):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    B.append(temp)

def matrixMul(A, B):
    if (len(A[0]) == len(B)):
        res = [[0] * len(B[0]) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    res[i][j] += A[i][k] * B[k][i]
        return res
    return False

res = matrixMul(A, B)
for i in range(len(res)):
    for j in range(len(res[0])):
        sys.stdout.write("%d"%res[i][j])
        if j <len(res[0])-1:
            sys.stdout.write(" ")
        elif j == len(res[0])-1 and i < len(res)-1:
            sys.stdout.write("\n")

"""
2 3 2 
1 2 3
1 2 3
1 1
1 1
1 1 
"""