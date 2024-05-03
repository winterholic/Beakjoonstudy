import sys
input = sys.stdin.readline
import heapq

classroom = []

N = int(input())

for i in range(N) :
    S, T = map(int, input().split()) # S에 시작해서 T에 끝나는 수업
    classroom.append((S, T))

classroom.sort()

ans = []
heapq.heappush(ans, classroom[0][1])

for i in range(1, N) :
    if classroom[i][0] < ans[0] :
        heapq.heappush(ans, classroom[i][1])
    else :
        heapq.heappop(ans)
        heapq.heappush(ans, classroom[i][1])

print(len(ans))