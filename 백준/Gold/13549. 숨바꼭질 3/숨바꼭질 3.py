import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

N, K = map(int, input().split())

queue = deque()
queue.append(N)

visited = [-1 for _ in range(100001)]
visited[N] = 0

while queue :
    x = queue.popleft()
    #print(visited[:20])
    if x == K :
        break

    x1 = x + 1
    x2 = x - 1
    x3 = 2 * x

    if (x3 >= 0 and x3 < 100001) :
        if(visited[x3] == -1) :
            visited[x3] = visited[x]
            queue.appendleft(x3)
    if (x2 >= 0 and x2 < 100001) :
        if(visited[x2] == -1) :
            visited[x2] = visited[x] + 1
            queue.append(x2)
    if (x1 >= 0 and x1 < 100001) :
        if(visited[x1] == -1) :
            visited[x1] = visited[x] + 1
            queue.append(x1)

print(visited[K])