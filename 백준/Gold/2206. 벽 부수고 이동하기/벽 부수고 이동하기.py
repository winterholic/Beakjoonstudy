import sys
from collections import deque

N, M = map(int, input().split())

graph = []

for i in range(N) :
    temp = list(map(int, input()))
    graph.append(temp)

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

#print(graph)
#print(visited1)
#print(visited2)
#print(visited)

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def BFS() :
    while queue :
        x, y, z = queue.popleft()
        if(x == N - 1 and y == M - 1) :
            return visited[x][y][z]
        for dir in direct :
            px = x + dir[0]
            py = y + dir[1]
            if(px < 0 or px >= N or py < 0 or py >= M) :
                continue
            if (graph[px][py] == 1 and z == 0) :
                visited[px][py][1] = visited[x][y][0] + 1
                queue.append((px, py, 1))
            elif (graph[px][py] == 0 and visited[px][py][z] == 0) :
                visited[px][py][z] = visited[x][y][z] + 1
                queue.append((px, py, z))
    return -1


"""for i in range(N) :
    for j in range(M) :
        print(visited[i][j], end = " ")
    print()
print()"""

print(BFS())