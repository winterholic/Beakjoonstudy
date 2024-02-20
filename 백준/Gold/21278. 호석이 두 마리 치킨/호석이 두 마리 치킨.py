import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

graph = [[0] * (101) for _ in range(101)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

edgenum = [0] * (N + 1)

for i in range(1, N + 1) :
    for j in range(1, N + 1) :
        if(graph[i][j] == 1) :
            edgenum[i] += 1

max_index = max(range(len(edgenum)), key=lambda i: edgenum[i])
# print(edgenum)
# print()
# print(max_index)
# print()

# for i in range(N + 1) :
#     for j in range(N + 1) :
#         print(graph[i][j], end = " ")
#     print()

combinations_list = list(combinations(range(1, N + 1), 2))
#print(combinations_list)

ans = 2100000000
ans1 = -1
ans2 = -1

for i in range(len(combinations_list)) :
    for1 = combinations_list[i][0]
    for2 = combinations_list[i][1]
    if(for1 != max_index and for2 != max_index) :
        continue
    #print(for1, for2)
    sumdata = 0
    for j in range(1, N + 1) :
        cur = j
        visited = [0] * (N + 1)
        times = 0
        while True :
            #print(cur, times)
            visited[cur] = 1
            #print(cur, for1, for2)
            if(cur == for1 or cur == for2) :
                sumdata += (times * 2)
                break
            flag = 0
            for k in range(1, N + 1) :
                if(graph[cur][k] == 1 and visited[k] == 0) :
                    cur = k
                    flag = 1
                    break
            times += 1
            if(flag == 0) :
                break
    
    if(sumdata < ans) :
        ans = sumdata
        ans1 = for1
        ans2 = for2

print(ans1, ans2, ans)