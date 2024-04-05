import sys
input = sys.stdin.readline

N, M = map(int, input().split())

tree = [[] for _ in range(N + 1)]
distance = []

for i in range(N - 1) :
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

for i in range(M) :
    a, b = map(int, input().split())
    distance.append((a, b))

#print(tree)

ans = 0

def DFS(froma, forb, dis) :
    global ans
    
    if froma == forb :
        ans = dis
        return
    
    for tf in tree[froma] :
        if visited[tf[0]] == 0 :
            visited[tf[0]] = 1
            DFS(tf[0], forb, dis + tf[1])


for a, b in distance :
    visited = [0] * (N + 1)
    ans = 0
    visited[a] = 1
    DFS(a, b, 0)
    print(ans)