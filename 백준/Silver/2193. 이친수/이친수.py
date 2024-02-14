N = int(input())

dp = [[0] * 2 for _ in range(N + 1)]

for i in range(1, N + 1) :
    if(i == 1) :
        dp[i][0] = 0
        dp[i][1] = 1
    elif(i == 2) :
        dp[i][0] = 1
        dp[i][1] = 0
    else :
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0]

print(sum(dp[N]))