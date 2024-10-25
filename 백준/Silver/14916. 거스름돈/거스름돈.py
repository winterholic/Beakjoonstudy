N = int(input())

dp = [1000001] * (N + 1)

if N >= 2:
    dp[2] = 1
if N >= 4:
    dp[4] = 2
if N >= 5:
    dp[5] = 1
if N >= 6:
    dp[6] = 3

for i in range(7, N + 1):
    dp[i] = min(dp[i - 2], dp[i - 5]) + 1

if dp[N] == 1000001:
    print(-1)
else:
    print(dp[N])
