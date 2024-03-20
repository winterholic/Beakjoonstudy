import sys
import heapq
input = sys.stdin.readline

N = int(input())

hw = []

for i in range(N) :
    d, w = map(int, input().split())
    hw.append([d, w])

hw.sort()
#print(hw)

ans = []

for i in range(N) :
    #print(ans)
    d = hw[i][0]
    w = hw[i][1]
    if(len(ans) < d) :
        #print('1', d, w)
        heapq.heappush(ans, w)
    else :
        #print('2', d, w)
        if(ans[0] < w) :
            heapq.heappop(ans)
            heapq.heappush(ans, w)

sumdata = sum(ans)
print(sumdata)            