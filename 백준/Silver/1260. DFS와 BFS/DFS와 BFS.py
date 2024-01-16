import sys
input = sys.stdin.readline
from collections import deque
#sys.setrecursionlimit(10 ** 6)

def DFS(index) :
    visited1[index] = True
    print(index, end = ' ')

    for i in range(1, N + 1):
        if(visited1[i] == False and numbers[index][i] == True) :
            DFS(i)

def BFS(index) :
    queue = deque([index])
    visited2[index] = True

    while queue :
        index = queue.popleft()
        print(index, end = ' ')

        for i in range(1, N + 1) :
            if(visited2[i] == False and numbers[index][i] == True) :
                visited2[i] = True
                queue.append(i)
                
N, M, V = map(int, input().split())

numbers = [[False] * 1001 for _ in range(1001)] #1000 x 1000

for i in range(M) :
    a, b = map(int, input().split())
    numbers[a][b] = True
    numbers[b][a] = True

visited1 = [False] * 1001
visited1[V] = True
visited2 = [False] * 1001
visited2[V] = True

DFS(V)
print()
BFS(V)