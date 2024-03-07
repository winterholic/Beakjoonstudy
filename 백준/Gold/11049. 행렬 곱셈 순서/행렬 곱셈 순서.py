import sys
input = sys.stdin.readline
INF = float('inf')

N = int(input())

matrix = []

for i in range(N) :
    a, b = map(int, input().split())
    matrix.append((a, b))

dp = [[0] * N for _ in range(N)]

for i in range(1, N) :
    for j in range(0, N - i) :
        if i == 1 :
            dp[j][j + i] = matrix[j][0] * matrix[j + 1][0] * matrix[j + 1][1]

        else :
            dp[j][j + i] = INF
            for k in range(j, j + i) :
                dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + (matrix[j][0] * matrix[k][1] * matrix[j + i][1]))

#print(dp)
print(dp[0][-1])