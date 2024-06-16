import sys
input = sys.stdin.readline
import heapq
INF = float("inf")

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]  

for i in range(m) :
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

st, ed = map(int, input().split())

distance = [INF] * (n + 1)
before = [0] * (n + 1)

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

    return

dijkstra(distance, st)
print(distance[ed])