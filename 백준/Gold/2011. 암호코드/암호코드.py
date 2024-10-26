N = list(map(int, input().rstrip()))

# print(N)

dp = [0] * (len(N) + 1)
dp[0] = 1
dp[1] = 1 if N[0] != 0 else 0 

ans = 0

if N[0] == 0:
    ans = 0
else:
    for i in range(1, len(N)):
        if N[i] > 0:
            dp[i + 1] += dp[i]
        
        if 10 <= N[i - 1] * 10 + N[i] <= 26:
            dp[i + 1] += dp[i - 1]
            
    ans = dp[len(N)] % 1000000

print(ans)
