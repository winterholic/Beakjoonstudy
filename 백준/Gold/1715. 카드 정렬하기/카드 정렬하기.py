import heapq

N = int(input())
card = []

for i in range(N):
    card.append(int(input()))

heapq.heapify(card)  # 최소 힙으로 변환

ans = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    temp = a + b
    ans += temp
    heapq.heappush(card, temp)

print(ans)