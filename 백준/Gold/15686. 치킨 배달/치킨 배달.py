N, M = map(int, input().split())

graph = []

for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

chicken = []
house = []

for i in range(N) :
    for j in range(N) :
        if(graph[i][j] == 1) :
            house.append((i,j))
        if(graph[i][j] == 2) :
            chicken.append((i,j))

ans = 100001

def cal_distance(h, c) :
    sum = 0
    for hloc in h :
        minimal = 100001
        hx = hloc[0]
        hy = hloc[1]
        for cloc in c :
            cx = cloc[0]
            cy = cloc[1]
            distance = abs(hx-cx) + abs(hy-cy)
            minimal = min(minimal, distance)
        sum += minimal
    return sum


def DFS(index, temp) :  
    global ans
    if(len(temp) == M) :
        #print(temp)
        cal_data = cal_distance(house, temp)
        ans = min(ans, cal_data)
        #print(ans, cal_data)
        return
    
    for i in range(index + 1, len(chicken)) :
        temp.append(chicken[i])
        DFS(i, temp)
        temp.pop()

temp = []
#print(chicken)
#print(house)
DFS(-1, temp)
print(ans)