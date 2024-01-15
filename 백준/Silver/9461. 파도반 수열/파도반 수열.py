import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 101

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
dp[9] = 7

for i in range (9, 101) :
    #print(i)
    dp[i] = dp[i - 1] + dp[i - 5]
    #print(dp[i])

for i in range(0, n) :
    a = int(input())
    print(dp[a])