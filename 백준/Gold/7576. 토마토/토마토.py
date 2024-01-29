import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

M, N = map(int, input().split())

store = []

for i in range(N) :
    temp = list(map(int, input().split()))
    store.append(temp)

#print(store)
    
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue = deque()

for i in range(N) :
    for j in range(M) :
        if (store[i][j] == 1) :
            queue.append((i, j))

def BFS() :
    while queue :
        x, y = queue.popleft()
        for dir in direct :
            px = x + dir[0]
            py = y + dir[1]
            if(px < 0 or px >= N or py < 0 or py >= M) :
                continue
            if(store[px][py] == 0) :
                store[px][py] = store[x][y] + 1
                queue.append((px, py))

BFS()

flag = 1
max = -1

for i in range(N) :
    for j in range(M) :
        if(store[i][j] == 0) :
            flag = 0
        if(max < store[i][j]) :
            max = store[i][j]

#print(store)

if(flag == 1) :
    print(max - 1)
else :
    print(-1)