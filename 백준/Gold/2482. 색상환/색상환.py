N = int(input())
K = int(input())

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1) :
    limited = i // 2
    for j in range(1, K + 1) :
        if (j == 1) :
            dp[i][j] = i
        elif(j <= limited) :
            dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1]) % 1000000003
        else :
            dp[i][j] = 0

# for i in range(len(dp)) :
#     print(*dp[i])

print(dp[N][K])