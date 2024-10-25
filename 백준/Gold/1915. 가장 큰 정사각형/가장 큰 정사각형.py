import sys

N, M = map(int, input().split())
# print(N, M)

arr = []
for i in range(N) :
    temp = list(input())
    arr.append(temp)

# print(arr)

dp = [[0] * M for _ in range(N)]

for i in range(M) :
    if arr[0][i] == '1' :
        dp[0][i] = 1

for i in range(N) :
    if arr[i][0] == '1' :
        dp[i][0] = 1

for i in range(1, N) :
    for j in range(1, M) :
        if arr[i][j] == '1' :
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

max_square = 0

for i in range(N) :
    if(max(dp[i]) > max_square) :
        max_square = max(dp[i])

print(max_square * max_square)