import sys
input = sys.stdin.readline
import heapq
INF = 1e8

N, M = map(int, input().split())

distance = [INF] * (N + 1)

graph = [[] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append([v, 1])
    graph[v].append([u, 1])

def dijkstra(start):
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

dijkstra(1)

#print(distance)
minhut = max(distance[2 :])
mincnt = 0
ans = -1

for i in range(2, N + 1) :
    if(minhut == distance[i]) :
        if(mincnt == 0) :
            ans = i
        mincnt += 1

print(ans, minhut, mincnt)