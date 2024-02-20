import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

N, M = map(int, input().split())

graph = [[0] * (101) for _ in range(101)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# for i in range(N + 1) :
#     for j in range(N + 1) :
#         print(graph[i][j], end = " ")
#     print()

combinations_list = list(combinations(range(1, N + 1), 2))
#print(combinations_list)

ans = 2100000000
ans1 = 2100000000
ans2 = 2100000000

def BFS(index) :
    queue = deque([index])
    visited = [0] * (N + 1)
    visited[index] = 1

    while queue :
        x = queue.popleft()

        for i in range(1, N + 1) :
            if(visited[i] > 0) :
                continue
            if(graph[x][i] == 1) :
                visited[i] = visited[x] + 1
                queue.append(i)

    return visited

for i in range(len(combinations_list)) :
    for1 = combinations_list[i][0]
    for2 = combinations_list[i][1]
    #print(for1, for2)
    sumdata = 0
    visited1 = BFS(for1)
    visited2 = BFS(for2)

    #print(visited1)
    #print(visited2)

    for i in range(1, N + 1) :
        if(i != for1 and i != for2) :
            sumdata += min(visited1[i] - 1, visited2[i] - 1) * 2
    #print("!!", i, sumdata);
    #print(sumdata)
    
    if(sumdata < ans) :
        ans, ans1, ans2 = sumdata, for1, for2

print(ans1, ans2, ans)