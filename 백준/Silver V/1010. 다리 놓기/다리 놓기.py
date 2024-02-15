import sys
input = sys.stdin.readline

n = int(input())

dp = [[0]*30 for _ in range(30)]

for i in range(0, 30) :
    for j in range(0, 30) :
        if i == 1 :
            dp[i][j] = j
        else :
            if i == j :
                dp[i][j] = 1
            elif i < j :
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

for i in range(0, n) :
    a, b = map(int, input().split())
    print(dp[a][b])