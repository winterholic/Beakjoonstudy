import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T) :
    k = int(input())
    hq1 = []
    hq2 = []
    memo = [1] * k

    for i in range(k) :
        a, b = input().split()
        b = int(b)
        
        if(a == 'I') :
            heapq.heappush(hq1, (b, i))
            heapq.heappush(hq2, (-b, i))

        elif(b == 1) :
            if hq2 :
                temp = heapq.heappop(hq2)
                memo[temp[1]] = 0
        elif(b == -1) :
            if hq1 :
                temp = heapq.heappop(hq1)
                memo[temp[1]] = 0

        while hq1 and memo[hq1[0][1]] == 0 :
            heapq.heappop(hq1)
        while hq2 and memo[hq2[0][1]] == 0 :
            heapq.heappop(hq2)

    if len(hq1) == 0 :
        print("EMPTY")
    else :
        print(-hq2[0][0], hq1[0][0])