import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

K = int(input())

apple = []

for i in range(K) :
    temp = list(map(int, input().split()))
    apple.append(temp)

#print(apple)
L = int(input())

change = []

for i in range(L) :
    a, b = input().split()
    a = int(a)
    temp = [a, b]
    change.append(temp)

graph = [[0] * N for _ in range(N)]

for i in range(K) :
    x, y = apple[i][0], apple[i][1]
    graph[x - 1][y - 1] = 1

direct = [[0, 1], [1, 0], [0, -1], [-1, 0]] # right, down, left, up
queue= deque()
px, py = 0 , 0
time = 0
i = 0
di = 0
queue.append((px, py))

while True :
    px = px + direct[di][0]
    py = py + direct[di][1]
    time += 1

    if(px < 0 or py < 0 or px >= N or py >= N) :
        #print("case1")
        break

    if((px, py) in queue) :
        #print("case2")
        break

    queue.append((px, py))

    if graph[px][py] == 0 :
        queue.popleft()
    
    else :
        graph[px][py] = 0

    if change[i][0] == time :
        if change[i][1] == 'L' :
            di = (di - 1) % 4
        elif change[i][1] == 'D' :
            di = (di + 1) % 4
        if i < len(change) - 1 :
            i += 1

print(time)