a = int(input())
dp = [0] * (a + 5)
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5

for i in range(5, a + 1) :
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[a] % 10007)
#print(dp[a])