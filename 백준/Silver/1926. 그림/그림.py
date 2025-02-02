from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(x, y):
    graph[x][y] = 0
    width = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                width += 1

    return width

cnt = 0
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            ans = max(ans, bfs(i, j))

print(cnt)
print(ans)