import sys
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N + 1)]

for i in range(N) :
    temp = list(map(int, input().split()))
    temp = temp[: -1]
    a = temp[0]
    for i in range(1, len(temp) - 1, 2) :
        b = temp[i]
        c = temp[i + 1]
        tree[a].append([b, c])
        tree[b].append([a, c])

distance = [-1] * (N + 1)
distance[0] = 0
distance[1] = 1

def DFS(start, cost) :
    for child in tree[start] :
        if distance[child[0]] == -1 :
            newcost = cost + child[1]
            distance[child[0]] = newcost
            DFS(child[0], newcost)

DFS(1, 0)

#print(distance)

max1 = distance.index(max(distance))
distance = [-1] * (N + 1)
distance[0] = 0
distance[max1] = 0
DFS(max1, 0)
#print(distance)
print(max(distance))