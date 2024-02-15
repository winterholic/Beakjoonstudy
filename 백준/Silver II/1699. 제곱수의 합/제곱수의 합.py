N = int(input())

dp = [i for i in range(N + 1)]

for i in range(1, N + 1) :
    for j in range(1, i) :
        if pow(j, 2) > i :
            break
        dp[i] = min(dp[i], dp[i - pow(j, 2)] + 1)

print(dp[N])