import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[float('inf')] * N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for i in range(M) :
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

def floydwarshall(n, graph) :
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

floydwarshall(N, graph)

cnt = 0

for i in range(N) :
    flag = 1
    for j in range(N) :
        if graph[i][j] == float("inf") and graph[j][i] == float("inf") :
            flag = 0
            break
    cnt += flag

print(cnt)