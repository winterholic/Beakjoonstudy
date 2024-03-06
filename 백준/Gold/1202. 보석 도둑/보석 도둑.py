import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())

jewely = []

for i in range(N) :
    a, b = map(int, input().split()) #무게,가격
    heapq.heappush(jewely, (a, b))

bag = []

for i in range(K) :
    c = int(input())
    bag.append(c)

bag.sort()

ans = 0

temp = []

for i in range(K) :
    while jewely and bag[i] >= jewely[0][0] :
        tmp = heapq.heappop(jewely)[1]
        heapq.heappush(temp, -tmp)
    if temp :
        ans -= heapq.heappop(temp)
    elif len(jewely) == 0 :
        break
    
print(ans)