import sys
input = sys.stdin.readline
import heapq
INF = 1e8

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]

for i in range(E) :
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

distance = [INF] * (V + 1)

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

dijkstra(K)

#print(distance)

for i in range(1, len(distance)) :
    if(distance[i] == INF) :
        print("INF")
    else :
        print(distance[i])