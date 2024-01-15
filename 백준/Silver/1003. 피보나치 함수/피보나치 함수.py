a = int(input())
dp = [0] * 45
dp[0] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(5, 45) :
    dp[i] = dp[i - 1] + dp[i - 2]

for i in range(0, a) :
    b = int(input())
    print(dp[b], dp[b + 1])