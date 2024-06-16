import sys
input = sys.stdin.readline
import heapq
INF = float("inf")

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]  

for i in range(m) :
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

st = 1

ed = n

ne_node1, ne_node2 = map(int, input().split())


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

node1_distance = [INF] * (n + 1)
node2_distance = [INF] * (n + 1)
node3_distance = [INF] * (n + 1)
dijkstra(node1_distance, st)
dijkstra(node2_distance, ne_node1)
dijkstra(node3_distance, ne_node2)

root1 = node1_distance[ne_node1] + node2_distance[ne_node2] + node3_distance[ed]
root2 = node1_distance[ne_node2] + node3_distance[ne_node1] + node2_distance[ed]

ans = min(root1, root2)
if ans < INF :
    print(ans)
else :
    print(-1)


# present = ed
# cnt = 1
# flag1 = 0
# flag2 = 0

# print(distance)
# print(before)

# while True :
#     if present == st :
#         break
#     if present == ne_node1 :
#         flag1 = 1
#     if present == ne_node2 :
#         flag2 = 1
#     present = before[present]
    

# if flag1 == 1 and flag2 == 1 :
#     print(distance[ed])
# else :
#     print(-1)