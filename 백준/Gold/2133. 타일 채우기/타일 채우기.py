N = int(input())

dp = [0] * 31

dp[0] = 0
dp[1] = 0
dp[2] = 3
dp[3] = 0
dp[4] = 11

for i in range(5, 31) :
    if(i % 2 == 1) :
        dp[i] = 0
    else :
        dp [i] = dp[i - 2] * 3 + 2
        for j in range(2, i - 2, 2) :
            dp[i] += dp[j] * 2

print(dp[N])