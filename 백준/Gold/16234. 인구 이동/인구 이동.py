import sys
from collections import deque
N, L, R = map(int, input().split())

country = []
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(N) :
    temp = list(map(int, input().split()))
    country.append(temp)

#print(country)

def BFS(x, y) :
    queue = deque()
    queue.append((x, y))

    new_arr = []
    new_arr.append((x, y))

    while queue:
        x, y = queue.popleft()
        for dir in direct:
            px = x + dir[0]
            py = y + dir[1]
            if(px < 0 or px >= N or py < 0 or py >= N) :
                continue
            if visited[px][py] == 0:
                if L <= abs(country[px][py] - country[x][y]) <= R:
                    visited[px][py] = 1
                    queue.append((px, py))
                    new_arr.append((px, py))

    return new_arr

cnt = 0
while True :
    visited = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                new_country = BFS(i, j)

                if len(new_country) > 1 :
                    flag = 1
                    
                    mean = sum([country[x][y] for x, y in new_country]) // len(new_country)
                        
                    for x,y in new_country:
                        country[x][y] = mean
    
    if flag == 0:
        break

    cnt += 1

print(cnt)