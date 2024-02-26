import sys
input = sys.stdin.readline
import heapq

N, M, K, X = map(int, input().split())

INF = 1e8

graph = [[] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append([v, 1])

# for i in range(N + 1) :
#     print(*graph[i])

distance = [INF] * (N + 1)
visited = [False] * (N + 1)

# def get_smallest_node():
#     min_val = INF
#     index = 0
#     for i in range(1, N + 1):
#         if distance[i] < min_val and not visited[i]: 
#             min_val = distance[i]
#             index = i
#     return index

# #print(graph)

# def dijkstra(start) :
#     distance[start] = 0
#     visited[start] = True

#     for g in graph[start] :
#         distance[g[0]] = g[1]

#     for i in range(N - 1) :
#         index = get_smallest_node()
#         visited[index] = True

#         for g in graph[index] :
#             if distance[g[0]] > distance[index] + g[1] :
#                 distance[g[0]] = distance[index] + g[1]

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 우선순위, 값 형태로 들어간다.
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

    if distance[now] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
      continue               # 따라서 다음으로 넘어간다.

    for i in graph[now]:     # 연결된 모든 노드 탐색
      if dist+i[1] < distance[i[0]]: # 기존에 입력되어있는 값보다 크다면
        distance[i[0]] = dist+i[1]   #
        heapq.heappush(q, (dist+i[1], i[0]))

dijkstra(X)

flag = 0
for i in range(len(distance)) :
    if(distance[i] == K) :
        print(i)
        flag = 1
        
if(flag == 0) :
    print(-1)