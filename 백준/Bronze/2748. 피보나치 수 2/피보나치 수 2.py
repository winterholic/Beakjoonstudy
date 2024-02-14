N = int(input())

dp = [0] * (N + 1)

for i in range(0, N + 1) :
    if(i == 0) :
        dp[i] = 0
    if(i == 1) :
        dp[i] = 1
    else :
        dp[i] = dp[i - 2] + dp[i - 1]

#print(dp)
print(dp[N])