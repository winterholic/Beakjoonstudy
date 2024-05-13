import sys
input = sys.stdin.readline

N = int(input())
tp = []
for i in range(N) :
    a, b = map(int, input().split())
    tp.append((a, b))

tp.sort()

dp = [1] * 100

for i in range(1, N) :
    for j in range(0, i) :
        if tp[j][1] < tp[i][1] :
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))