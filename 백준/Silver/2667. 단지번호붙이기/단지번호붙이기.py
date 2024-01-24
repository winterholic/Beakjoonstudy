N = int(input())

graph = []

for i in range(N) :
    temp = list(map(int, input()))
    graph.append(temp)

cnt = 0
ans = []

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def DFS(x, y) :
    global cnt
    if(x < 0 or y < 0 or x >= N or y >= N) :
        return
    
    if graph[x][y] == 1 :
        cnt += 1
        graph[x][y] = 0
        for px, py in direct :
            DFS(x + px, y + py)

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            DFS(i, j)
            ans.append(cnt)
            cnt = 0

ans = sorted(ans)

print(len(ans))
for i in range(len(ans)):
    print(ans[i])

"""for i in range(N) :
    for j in range(N) :
        print(graph[i][j], end = "")
    print()"""