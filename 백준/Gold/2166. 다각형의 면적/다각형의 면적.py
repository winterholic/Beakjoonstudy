import sys
input = sys.stdin.readline

vertexs = []

N = int(input())

for i in range(N) :
    a, b = map(int, input().split())
    vertexs.append((a, b))

vertexs.append((vertexs[0][0], vertexs[0][1]))

sumx = 0
sumy = 0

for i in range(N) :
    sumx += vertexs[i][0] * vertexs[i + 1][1]
    sumy += vertexs[i][1] * vertexs[i + 1][0]

ans = (sumx - sumy) / 2

ans = abs(round(ans, 1))

print(ans)