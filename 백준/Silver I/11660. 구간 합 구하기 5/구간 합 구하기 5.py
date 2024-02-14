import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for i in range(N) :
    temp = list(map(int, input().split()))
    graph.append(temp)

"""print("-----------------------------------------------")
for i in range(N) :
    for j in range(N) :
        print(graph[i][j], end = " ")
    print()
print("-----------------------------------------------")
"""
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1) :
    for j in range(1, N + 1) :
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + graph[i - 1][j - 1]

"""print("-----------------------------------------------")
for i in range(N) :
    for j in range(N) :
        print(dp[i][j], end = " ")
    print()
print("-----------------------------------------------")"""

for i in range(M) :
    x1, y1, x2, y2 = map(int, input().split())

    ans = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(ans)