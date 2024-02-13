N = int(input())
street = list(input())

ans = 0

k = 0

dp = [999999999] * N

dp[0] = 0

for i in range(1, N) :
    for j in range(0, i) :
        if(street[i] == 'B' and street[j] == 'J') :
            dp[i] = min(dp[j] + (i - j) * (i - j), dp[i])
        elif(street[i] == 'O' and street[j] == 'B') :
            dp[i] = min(dp[j] + (i - j) * (i - j), dp[i])
        elif(street[i] == 'J' and street[j] == 'O') :
            dp[i] = min(dp[j] + (i - j) * (i - j), dp[i])


if(dp[N - 1] == 999999999) :
    print(-1)
else :
    print(dp[N - 1])