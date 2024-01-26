from collections import deque

N, M = map(int, input().split())

graph = []

for i in range(N) :
    temp = list(map(int, input()))
    graph.append(temp)

#print(graph)

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def BFS(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()

        for dir in direct :
            px = x + dir[0]
            py = y + dir[1]

            if px < 0 or px >= N or py < 0 or py >= M :
                continue

            if graph[px][py] == 0 :
                continue

            if graph[px][py] == 1 :
                graph[px][py] = graph[x][y] + 1
                queue.append((px, py))

BFS(0, 0)
#print(graph)
print(graph[N - 1][M - 1])