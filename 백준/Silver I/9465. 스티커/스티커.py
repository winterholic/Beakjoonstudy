import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    sticker = []
    temp1 = list(map(int, input().split()))
    temp2 = list(map(int, input().split()))
    sticker.append(temp1)
    sticker.append(temp2)

    dp = [[0] * N for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    if N == 1 :
        ans = max(dp[0][0], dp[1][0])

    elif N == 2:
        dp[0][1] = sticker[1][0] + sticker[0][1]
        dp[1][1] = sticker[0][0] + sticker[1][1]
        ans = max(dp[0][1], dp[1][1])
    
    else :
        dp[0][1] = sticker[1][0] + sticker[0][1]
        dp[1][1] = sticker[0][0] + sticker[1][1]
        for i in range(2, N) :
            dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + sticker[0][i]
            dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + sticker[1][i]
        ans = max(dp[0][N - 1], dp[1][N - 1])

    #print(dp)
    
    print(ans)