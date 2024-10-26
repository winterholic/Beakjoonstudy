import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())

forest = []

for i in range(N) :
    forest.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def DFS(x, y):
    if dp[x][y] != 0 :
        return dp[x][y]
    dp[x][y] = 1
    for dir in direct :
        dx = x + dir[0]
        dy = y + dir[1]
        if(0 <= dx < N and 0 <= dy < N and forest[dx][dy] > forest[x][y]) :
            dp[x][y] = max(dp[x][y], DFS(dx, dy) + 1)
    return dp[x][y]

ans = 0

for i in range(N) :
    for j in range(N) :
        ans = max(ans, DFS(i, j))

print(ans)