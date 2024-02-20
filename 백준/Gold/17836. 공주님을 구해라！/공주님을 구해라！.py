import sys
input = sys.stdin.readline
from collections import deque

N, M, T = map(int, input().split())

graph = []

for _ in range(N) :
    temp = list(map(int, input().split()))
    graph.append(temp)

#print(graph)
#print()

x = 0
y = 0

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

queue = deque()
queue.append((x, y))

visited = [[0] * M for _ in range(N)]

while queue :
    x, y = queue.popleft()
    if(x == N - 1 and y == M - 1) :
        break

    for dir in direct :
        px = x + dir[0]
        py = y + dir[1]
        
        if(px < 0 or py < 0 or px >= N or py >= M) :
            continue

        if(visited[px][py] == 0) :
            if(graph[px][py] == 0) :
                visited[px][py] = visited[x][y] + 1
                queue.append((px, py))

visited2 = [[0] * M for _ in range(N)]
queue = deque()
queue.append((0, 0))

sword = 0
flag = 0

while queue :
    if(flag == 1) :
        break
    x, y = queue.popleft()
    if(x == N - 1 and y == M - 1) :
        break

    for dir in direct :
        #print(visited2)
        px = x + dir[0]
        py = y + dir[1]
        
        if(px < 0 or py < 0 or px >= N or py >= M) :
            continue

        if(sword == 0) :
            if(graph[px][py] == 0) :
                if(visited2[px][py] == 0) :
                    visited2[px][py] = visited2[x][y] + 1
                    queue.append((px, py))

            elif (graph[px][py] == 2) :
                if(visited2[px][py] == 0) :
                    visited2[N - 1][M - 1] = visited2[x][y] + 1 + (N - 1 - px) + (M - 1 - py)
                    #print(visited2[x][y] + 1, (N - 1 - px), (M - 1 - py))
                    flag = 1
                    break

# print("__________________________________________________")     
# for i in range(N) :
#     for j in range(M) :
#         print(visited[i][j], end = " ")
#     print()
# print("__________________________________________________")
# for i in range(N) :
#     for j in range(M) :
#         print(visited2[i][j], end = " ")
#     print()
# print("__________________________________________________")

ans1 = visited[N - 1][M - 1]
ans2 = visited2[N - 1][M - 1]

if(ans1 == 0 and ans2 == 0) :
    print("Fail")
else :
    if(ans1 == 0) :
        if(ans2 > T) :
            print("Fail")
        else :
            print(ans2)
    else :
        ans3 = min(ans1, ans2)
        if(ans3 > T) :
            print("Fail")
        else :
            print(ans3)