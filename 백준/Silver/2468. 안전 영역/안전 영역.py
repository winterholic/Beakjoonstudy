import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())

area = []

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def DFS(x, y, graph, N) :
    global cnt
    if(x < 0 or y < 0 or x >= N or y >= N) :
        return
    
    if graph[x][y] == 1 :
        cnt += 1
        graph[x][y] = 0
        for px, py in direct :
            DFS(x + px, y + py, graph, N)

for i in range(N) :
    temp = list(map(int, input().split()))
    area.append(temp)

max = -1

for i in range(0, 101) :
    cnt = 0
    ans = []
    graph = [[False] * (N) for _ in range(N)]
    for j in range(N) :
        for k in range(N) :
            if(area[j][k] > i) :
                graph[j][k] = True
    for j in range(N) :
        for k in range(N) :
            if(graph[j][k] == True) :
                DFS(j, k, graph, N)
                ans.append(cnt)
                cnt = 0
    if(max < len(ans)) :
        max = len(ans)

print(max)