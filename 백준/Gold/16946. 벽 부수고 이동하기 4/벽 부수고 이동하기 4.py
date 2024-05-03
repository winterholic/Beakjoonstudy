from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

ans = [[set() for _ in range(M)] for _ in range(N)]
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0] * M for _ in range(N)]
groups = [[0] * M for _ in range(N)]
group_cnt = 1
gd = {}
gd[0] = 0

def BFS(x, y) :
    queue = deque()
    queue.append((x, y))
    cnt = 1
    while queue :
        x, y = queue.popleft()
        groups[x][y] = group_cnt
        for dir in direct :
            dx = x + dir[0]
            dy = y + dir[1]
            if dx < 0 or dy < 0 or dx >= N or dy >= M :
                continue
            if visited[dx][dy] == 0 and graph[dx][dy] == 0 :
                visited[dx][dy] = 1
                queue.append((dx, dy))
                cnt += 1
    return cnt

for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 0 and visited[i][j] == 0 :
            visited[i][j] = 1
            data = BFS(i, j)
            gd[group_cnt] = data
            group_cnt += 1

for i in range(N) :
    for j in range(M) :
        tempset = set()
        if graph[i][j] :
            for dir in direct :
                dx = i + dir[0]
                dy = j + dir[1]
                if dx < 0 or dy < 0 or dx >= N or dy >= M :
                    continue
                tempset.add(groups[dx][dy])
            for ts in tempset :
                graph[i][j] += gd[ts]
                graph[i][j] %= 10

# print("____________________________________")

for i in range(N) :
    for j in range(M) :
        print(graph[i][j], end = "")
    print()