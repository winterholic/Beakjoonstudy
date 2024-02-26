import sys
input = sys.stdin.readline
INF = 1e8
from copy import deepcopy

N = int(input())

graph = []

for i in range(N) :
    temp = list(map(int, input().split()))
    graph.append(temp)

answer = []

for i in range(N) :
    temp = []
    for j in range(N) :
        if(graph[i][j] == 1) :
            temp.append(1)
        else :
            temp.append(INF)
    answer.append(temp)

#print(answer)

for i in range(N) :
    for j in range(N) :
        for k in range(N) :
            if(answer[j][i] + answer[i][k] < answer[j][k]) :
                answer[j][k] = answer[j][i] + answer[i][k]

#print(answer)

for i in range(N) :
    for j in range(N) :
        if(answer[i][j] != INF) :
            print(1, end = " ")
        else :
            print(0, end = " ")
    print()