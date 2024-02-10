import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

direct = [[0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, -1], [0, 0, 1]]
queue = deque()


def BFS() :
    while queue :
        z, x, y = queue.popleft()
        for dir in direct :
            px = x + dir[0]
            py = y + dir[1]
            pz = z + dir[2]

            if(px < 0 or px >= N or py < 0 or py >= M or pz < 0 or pz >= H) :
                continue

            if graph[pz][px][py] == 0 :
                graph[pz][px][py] = graph[z][x][y] + 1
                queue.append((pz, px, py))


for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if graph[i][j][k] == 1 :
                queue.append((i, j, k))

BFS()

flag = 1
max = -1

for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if(graph[i][j][k] == 0) :
                flag = 0
            if(max < graph[i][j][k]) :
                max = graph[i][j][k]

#print(graph)

if(flag == 1) :
    print(max - 1)
else :
    print(-1)