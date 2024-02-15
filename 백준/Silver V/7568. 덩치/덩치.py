import sys
input = sys.stdin.readline

N = int(input())

size = []
rank = [1] * N

for _ in range(N) :
    temp = list(map(int, input().split()))
    size.append(temp)

for i in range(N) :
    for j in range(N) :
        if(size[i][0] < size[j][0] and size[i][1] < size[j][1]) :
            rank[i] += 1

for i in range(N) :
    print(rank[i] ,end = " ")