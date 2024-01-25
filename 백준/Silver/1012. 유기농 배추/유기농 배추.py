import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def DFS(x, y, N, M, graph) :
    global cnt
    if(x < 0 or y < 0 or x >= N or y >= M) :
        return
    
    if graph[x][y] == True :
        cnt += 1
        graph[x][y] = False
        for px, py in direct :
            DFS(x + px, y + py, N, M, graph)


for i in range(T) :
    M, N, K = map(int, input().split())
    cnt = 0
    ans = []
    graph = [[False] * (M) for _ in range(N)]
    for j in range(K) :
        a, b = map(int, input().split())
        graph[b][a] = True
    #print(graph)
    for j in range(N) :
        for k in range(M) :
            if (graph[j][k] == True) :
                DFS(j, k, N, M, graph)
                ans.append(cnt)
                cnt = 0
    
    #ans = sorted(ans)
    #print(ans)
    print(len(ans))