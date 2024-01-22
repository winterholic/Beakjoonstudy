from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
skill = list(map(int, input().split()))
initiall = []
initiall = deque()

skill.reverse()

for i in range(N) :
    if(skill[i] == 1) :
        initiall.appendleft(i + 1)
    elif(skill[i] == 2) :
        temp = initiall.popleft()
        initiall.appendleft(i + 1)
        initiall.appendleft(temp)
    else :
        initiall.append(i + 1)

for ini in initiall:
    print(ini, end = " ")