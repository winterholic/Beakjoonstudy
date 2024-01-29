import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

treasure = []

for i in range(N):
    temp = input()
    treasure.append(temp)

#print(treasure)

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = deque()

def BFS(x, y) :
    graph = [[0] * M for _ in range(N)]
    queue.append([x, y])
    graph[x][y] = 1
    cnt = 0
    while queue :
        x, y = queue.popleft()
        for dir in direct :
            px = x + dir[0]
            py = y + dir[1]
            if(px < 0 or px >= N or py < 0 or py >= M) :
                continue
            if(graph[px][py] == 0 and treasure[px][py] == 'L') :
                graph[px][py] = graph[x][y] + 1
                cnt = max(cnt, graph[px][py])
                queue.append([px, py])
    return cnt - 1

max_data = -1

for i in range(N) :
    for j in range(M) :
        if(treasure[i][j] == 'L') :
            max_data = max(max_data, BFS(i, j))
            #print(cloned_graph)

print(max_data)