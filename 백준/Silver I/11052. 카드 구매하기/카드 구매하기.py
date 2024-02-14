import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

card = deque(map(int, input().split()))
card.appendleft(0)
card = list(card)

#print(card)

dp = [0] * (N + 1)

for i in range(1, N + 1) :
    for j in range(1, i + 1) :
        dp[i] = max(dp[i], card[j] + dp[i - j])

print(dp[N])