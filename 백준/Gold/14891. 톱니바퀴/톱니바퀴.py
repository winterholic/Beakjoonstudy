import sys
#input = sys.stdin.readline
from collections import deque

array = []

for i in range(4) :
    temp = deque(list(map(int, input())))
    array.append(temp)

K = int(input())

#print(array)

def right(a, b) :
    if a == 4 :
        return
    
    if array[a][6] != array[a - 1][2] :
        right(a + 1, -b)
        array[a].rotate(b)

def left(a, b) :
    if a == -1 :
        return

    if array[a + 1][6] != array[a][2] :
        left(a - 1, -b)
        array[a].rotate(b)

for i in range(K) :
    a, b = map(int, input().split())
    a = a - 1
    left(a - 1, -b)
    right(a + 1, -b)
    array[a].rotate(b)

score = 0
for i in range(4) :
    if array[i][0] == 1 :
        if i == 0 :
            score += 1
        if i == 1 :
            score += 2
        if i == 2 :
            score += 4
        if i == 3 :
            score += 8

print(score)