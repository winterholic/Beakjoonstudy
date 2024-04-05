K = int(input())
building = list(map(int, input().split()))

cbt = [[] for _ in range(K)] #complete binary tree

def DFS(thislist, order) :
    if order == K :
        return
    
    mid = len(thislist) // 2
    #print(order, mid, thislist)
    cbt[order].append(thislist[mid])

    DFS(thislist[0 : mid], order + 1)
    DFS(thislist[mid + 1 :], order + 1)

DFS(building, 0)

for c in cbt :
    print(*c)