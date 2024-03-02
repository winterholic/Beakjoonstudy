import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

graph = []

dp = [[-1] * M for _ in range(N)]

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for i in range(N) :
    temp = list(map(int, input().split()))
    graph.append(temp)

def DFS(x, y) :
    if x == N - 1 and y == M - 1 :
        return 1
    
    if dp[x][y] == -1 :
        dp[x][y] = 0
        for dir in direct :
            px = x + dir[0]
            py = y + dir[1]
            if(px < 0 or py < 0 or px >= N or py >= M) :
                continue
            if(graph[x][y] > graph[px][py]) :
                dp[x][y] += DFS(px, py)

    return dp[x][y]

ans = DFS(0, 0)
print(ans)