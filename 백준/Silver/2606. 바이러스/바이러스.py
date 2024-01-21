N = int(input())
K = int(input())

graph = [[False] * (N + 1) for _ in range(N + 1)] # (N + 1) x (N + 1)

for i in range(K) :
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (N + 1)

cnt = -1

def DFS(index) :
    global cnt
    visited[index] = True
    cnt += 1

    for i in range(1, N + 1):
        if(visited[i] == False and graph[index][i] == True) :
            DFS(i)

DFS(1)

print(cnt)