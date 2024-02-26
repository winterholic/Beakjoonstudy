import sys
input = sys.stdin.readline
INF = 1e8

def bellmanford(start, N) :
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    for i in range(1, N + 1) :
        for j in range(1, N + 1) :
            for next, cost in graph[j] :
                if distance[next] > distance[j] + cost :
                    distance[next] = distance[j] + cost
                    if i == N - 1:
                        return True
    return False

T = int(input())

for _ in range(T) :
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M) :
        S, E, T = map(int, input().split())
        graph[S].append([E, T])
        graph[E].append([S, T])

    for _ in range(W) :
        S, E, T = map(int, input().split())
        graph[S].append([E, -T])

    if bellmanford(1, N) :
        print("YES")

    else :
        print("NO")