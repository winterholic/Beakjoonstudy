import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())

graph = []

for i in range(N) :
    temp = list(map(int, input().split()))
    graph.append(temp)

zerolist = []

for i in range(N) :
    for j in range(M) :
        if(graph[i][j] == 0) :
            zerolist.append((i, j))

# wall = list(combinations(range(0, len(zerolist)), 3))
wall = list(combinations(zerolist, 3))

viruslist = []

for i in range(N) :
    for j in range(M) :
        if(graph[i][j] == 2) :
            viruslist.append((i, j))


#print(wall)
#print(zerolist)

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

ans = 0

def VIRUS(queue, tempgraph, visited) :    
    while queue :
        x, y = queue.popleft()
        tempgraph[x][y] = 2

        for dir in direct :
            px = x + dir[0]
            py = y + dir[1]

            if px < 0 or px >= N or py < 0 or py >= M :
                continue

            if visited[px][py] == -1 and tempgraph[px][py] == 0 :
                queue.append((px, py))
                visited[x][y] = 1

for w in wall :
    tempgraph = copy.deepcopy(graph)
    for wx, wy in w :
        tempgraph[wx][wy] = 1

    visited = [[-1] * M for _ in range(N)]
    queue = deque()

    for x, y in viruslist :
        queue.append((x, y))

    VIRUS(queue, tempgraph, visited)

    cnt = 0

    for i in range(N) :
        for j in range(M) :
            if(tempgraph[i][j] == 0) :
                cnt += 1

    if cnt > ans :
        ans = cnt

print(ans)