import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

tem = list(map(int, input().split()))
graph = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a - 1][b - 1] = l
    graph[b - 1][a - 1] = l

def floydwarshall(n, graph) :
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

floydwarshall(n, graph)

max_tem = 0
for i in range(n):
    this_tem = 0
    for j in range(n) :
        if graph[i][j] <= m :
            this_tem += tem[j]
    max_tem = max(max_tem, this_tem)

print(max_tem)