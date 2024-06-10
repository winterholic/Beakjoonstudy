import sys
input = sys.stdin.readline
import heapq
INF = float("inf")

direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dijkstra():
    q = []
    distance = [[INF] * N for _ in range(N)]
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        dist, x, y = heapq.heappop(q)

        if x == N - 1 and y == N - 1:
            print("Problem " + str(cnt) + ":", str(distance[x][y]))
            break

        for i in range(4):
            nx = x + direct[i][0]
            ny = y + direct[i][1]

            if 0 <= nx < N and 0 <= ny < N :
                cost = dist + graph[ny][nx]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

cnt = 1

while True:
    N = int(input())
    if N == 0 :
        sys.exit(0)
    graph = []
    for i in range(N) :
        temp = list(map(int, input().split()))
        graph.append(temp)
    dijkstra()
    cnt += 1