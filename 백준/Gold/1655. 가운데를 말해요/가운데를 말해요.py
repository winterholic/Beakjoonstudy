import sys
input = sys.stdin.readline
import heapq

maxhq = []
minhq = []
N = int(input())

for i in range(N):
    num = int(input())
    if len(maxhq) == len(minhq):
        heapq.heappush(maxhq, -num)
    else:
        heapq.heappush(minhq, num)

    if minhq and (-maxhq[0] > minhq[0]):
        mindata = heapq.heappop(minhq)
        maxdata = heapq.heappop(maxhq)
        heapq.heappush(maxhq, -mindata)
        heapq.heappush(minhq, -maxdata)
        
    #print("center : ", abs(maxhq[0]))
    print(-maxhq[0])