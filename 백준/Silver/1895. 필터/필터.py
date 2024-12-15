N, M = map(int, input().split())

graph = []

for i in range(N) :
    graph.append(list(map(int, input().split())))

T = int(input())

def filtering(x, y):
    values = [
        graph[x - 1][y - 1], graph[x - 1][y], graph[x - 1][y + 1],
        graph[x][y - 1],     graph[x][y],     graph[x][y + 1],
        graph[x + 1][y - 1], graph[x + 1][y], graph[x + 1][y + 1]
    ]
    values.sort()
    return values[4]

J = []

for i in range(1, N - 1) :
    temp = []
    for j in range(1, M - 1) :
        temp.append(filtering(i, j))
    J.append(temp)

cnt = 0

for i in range(N - 2) :
    for j in range(M - 2) :
        if J[i][j] >= T :
            cnt += 1

#print(J)

print(cnt)