import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for i in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def DFS(index) :
    visited[index] = True
    for i in range(1, N + 1) :
        if(graph[index][i] == True and visited[i] == False) :
            DFS(i)
            
cnt = 0
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)