import sys
input = sys.stdin.readline
INF = 1e8
from copy import deepcopy

n = int(input())
m = int(input())

graph = [[INF] * n for _ in range(n)]
path = [[()] * n for _ in range(n)]
# path = [[set() for _ in range(n)] for _ in range(n)]

for i in range(m) :
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)
    path[a - 1][b - 1] = (a - 1, b - 1)
    # path[a - 1][b - 1].add((a - 1, b - 1))

answer = deepcopy(graph)

for i in range(n) :
    answer[i][i] = 0

def floydwarshall():
    for i in range(n) :
        for j in range(n) :
            for k in range(n) :
                if(answer[j][i] + answer[i][k] < answer[j][k]) :
                    answer[j][k] = answer[j][i] + answer[i][k]
                    path[j][k] = path[j][i] + path[i][k][1:]

floydwarshall()

# print("_______________________________________________________________________")

for i in range(n) :
    for j in range(n) :
        if answer[i][j] == INF :
            print(0, end = " ")
        else :
            print(answer[i][j], end = " ")
    print()

for i in range(n) :
    for j in range(n) :
        print(len(path[i][j]), end = " ")
        for k in range(len(path[i][j])) :
            print(path[i][j][k] + 1, end = " ")
        print()