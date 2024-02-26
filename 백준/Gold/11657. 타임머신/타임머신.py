import sys
input = sys.stdin.readline
INF = 1e8

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

distance = [INF for _ in range(N + 1)]

def bellmanford(start, N) :
    distance[start] = 0
    for i in range(1, N + 1) :
        for j in range(1, N + 1) :
            for next, cost in graph[j] :
                if distance[j] != INF and distance[next] > distance[j] + cost :
                    distance[next] = distance[j] + cost
                    if i == N - 1 and N != 2:
                        return True
    return False
    
for _ in range(M) :
    A, B, C = map(int, input().split())
    graph[A].append([B, C])

if bellmanford(1, N) :
    #print("DD")
    print(-1)
else :
    for i in range(2, N + 1) :
        if distance[i] == INF :
            print(-1)
        else :
            print(distance[i])