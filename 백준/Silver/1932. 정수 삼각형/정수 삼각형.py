import sys
input = sys.stdin.readline

n = int(input())

triangle = []

for i in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)

dp = [[0] * (i + 1) for i in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        if i == n - 1:
            dp[i][j] = triangle[i][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

print(dp[0][0])