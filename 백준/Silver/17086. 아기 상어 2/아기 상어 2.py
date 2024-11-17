from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N) :
    temp = list(map(int, input().split()))
    graph.append(temp)

answer = [[0] * M for _ in range(N)]

direct = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]] 

def BFS(x, y) :
    queue = deque()
    visited = [[0] * M for _ in range(N)]
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 1 :
            return visited[x][y]
        for dir in direct :
            px = x + dir[0]
            py = y + dir[1]
            if(0 <= px < N and 0 <= py < M and visited[px][py] == 0) :
                visited[px][py] = visited[x][y] + 1
                queue.append((px, py))

for i in range(N) :
    for j in range(M) :
        answer[i][j] = BFS(i, j)

# print(answer)
ans = 0
for i in range(N) :
    ans = max(ans, max(answer[i]))
print(ans)