import sys
input = sys.stdin.readline
import heapq

N = int(input())

candidate = []

dasom = int(input())

for i in range(N - 1) :
    candidate.append(-(int(input())))

if(N == 1) :
    print(0)
    sys.exit(0)

heapq.heapify(candidate)
#print(candidate)

cnt = 0

while(True) :
    #print(-candidate[0], dasom)
    if -candidate[0] < dasom :
        break
    cnt += 1
    dasom += 1
    candidate[0] += 1
    heapq.heapify(candidate)
    #print(candidate)

print(cnt)