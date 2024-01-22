N, M = map(int, input().split())

A = []
B = []
C = [[0] * M for _ in range(N)]

for i in range(N) :
    temp = list(map(int, input().split()))
    A.append(temp)

for i in range(N) :
    temp = list(map(int, input().split()))
    B.append(temp)

for i in range(N) :
    for j in range(M) :
        C[i][j] = A[i][j] + B[i][j]

for i in range(N) :
    for j in range(M) :
        print(C[i][j], end = " ")
    print()