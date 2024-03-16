import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

visited = [False] * (N)

ans = 0

for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(start, depth) :
    global ans
    visited[start] = True
    if depth == 4:
        ans = 1
        return
    for i in graph[start] :
        if visited[i] == False :
            DFS(i, depth + 1)
    visited[start] = False

for i in range(N) :
    DFS(i, 0)
    if(ans == 1) :
        break

print(ans)