import sys
input = sys.stdin.readline
import heapq
INF = float("inf")
direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]

M, N = map(int, input().split())

graph = []

for i in range(N) :
    temp = list(map(int, input().rstrip()))
    graph.append(temp)

def BFS():
    q = []
    distance = [[INF] * M for _ in range(N)]
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        dist, x, y = heapq.heappop(q)
        # print(dist, x, y)

        if x == N - 1 and y == M - 1:
            print(distance[x][y])
            # print(distance)
            break

        for i in range(4):
            nx = x + direct[i][0]
            ny = y + direct[i][1]

            if 0 <= nx < N and 0 <= ny < M :
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny] :
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

# print(graph)

BFS()

# print(graph)