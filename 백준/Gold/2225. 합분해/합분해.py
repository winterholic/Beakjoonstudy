N, K = map(int ,input().split())

dp = [[0] * 201 for _ in range(201)]
for i in range(1, 201) :
    dp[1][i] = 1

for i in range(2, 201) :
    for j in range(1, 201) :
        if(j == 1) :
            dp[i][j] = i
        else :
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000

print(dp[K][N])