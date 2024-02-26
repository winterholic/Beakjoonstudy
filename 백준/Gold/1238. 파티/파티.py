import sys
input = sys.stdin.readline
import heapq
INF = 1e8

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M) :
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def dijkstra(distance, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue :
        dist, minindex = heapq.heappop(queue)

        if distance[minindex] < dist :
            continue

        for g in graph[minindex] :
            if dist + g[1] < distance[g[0]] :
                distance[g[0]] = dist + g[1]
                heapq.heappush(queue, (dist + g[1], g[0]))

    return distance

Xdistance = [INF] * (N + 1)
ans = [0] * (N + 1)
Xdistance = dijkstra(Xdistance, X)

for i in range(1, N + 1) :
    ans[i] += Xdistance[i]

for i in range(1, N + 1) :
    if i != X :
        tempdistance = [INF] * (N + 1)
        tempdistance = dijkstra(tempdistance, i)
        ans[i] += tempdistance[X]

print(max(ans))