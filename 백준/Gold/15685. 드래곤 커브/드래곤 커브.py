import sys
input = sys.stdin.readline

N = int(input())

commend = []

for _ in range(N) :
    temp = list(map(int, input().split()))
    commend.append(temp)

graph = [[0] * 101 for _ in range(101)]
direct = [[1, 0], [0, -1], [-1, 0], [0, 1]]

# 0 : right , 1 : up , 2 : left , 3 : down

for i in range(N) :
    x = commend[i][0]
    y = commend[i][1]
    d = commend[i][2]
    g = commend[i][3]

    graph[x][y] = 1

    dragoncurve = [d]

    for j in range(g) :
        for k in range(len(dragoncurve) - 1, -1, -1) :
            dragoncurve.append((dragoncurve[k] + 1) % 4)

    for j in range(len(dragoncurve)) :
        px = x + direct[dragoncurve[j]][0]
        py = y + direct[dragoncurve[j]][1]
        if x < 0 or y < 0 or x > 100 or y > 100 :
            continue
        
        graph[px][py] = 1
        x = px
        y = py

cnt = 0
for i in range(100) :
    for j in range(100) :
        if graph[i][j] and graph[i][j + 1] and graph[i + 1][j] and graph[i + 1][j + 1] :
            cnt += 1

print(cnt)