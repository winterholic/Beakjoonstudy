import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

temp_list = [0] * (M + 2)
graph.append(temp_list)

for _ in range(N) :
    temp = list(map(int, input().split()))
    temp.insert(0, 0)
    temp.append(0)
    graph.append(temp)

graph.append(temp_list)

# for g in graph :
#     print(*g)

dp = [[0] * (M + 2) for _ in range(N + 2)]

# print()
# for d in dp :
#     print(*d)

for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + graph[i][j]

# print()
# for d in dp :
#     print(*d)

print(dp[N][M])