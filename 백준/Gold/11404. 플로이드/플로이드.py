import sys
input = sys.stdin.readline
INF = 1e8
from copy import deepcopy

n = int(input())
m = int(input())

graph = [[INF] * n for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if(i == j) :
            graph[i][j] = 0

for i in range(m) :
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)

# print(graph)
answer = deepcopy(graph)
# print(answer)

def floydwarshall():
    for i in range(n) :
        for j in range(n) :
            for k in range(n) :
                if(answer[j][i] + answer[i][k] < answer[j][k]) :
                    answer[j][k] = answer[j][i] + answer[i][k]

floydwarshall()

for i in range(n) :
    for j in range(n) :
        if(answer[i][j] == INF) :
            print(0, end = " ")
        else :
            print(answer[i][j], end = " ")
    print()