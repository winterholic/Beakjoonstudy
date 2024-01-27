import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

direct = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

I = int(input())

for i in range(I) :
    N = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    x = sx
    y = sy
    queue = deque([(sx, sy)])
    graph = [[0] * N for _ in range(N)]
    graph[sx][sy] = 1

    while queue :
        x, y = queue.popleft()

        if(x == ex and y == ey) :
            break

        for dir in direct :
            px = x + dir[0]
            py = y + dir[1]

            if px < 0 or px >= N or py < 0 or py >= N :
                continue

            if graph[px][py] == 0 :
                graph[px][py] = graph[x][y] + 1
                queue.append((px, py))
    
    print(graph[ex][ey] - 1)