import sys
input = sys.stdin.readline

N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]

ans = 2100000000

for j in range(3) :
    dp = [[0] * 3 for _ in range(N)]
    dp[0][0] = 2100000000
    dp[0][1] = 2100000000
    dp[0][2] = 2100000000
    dp[0][j] = house[0][j]

    for i in range (1, N) :
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + house[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + house[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + house[i][2]

    # print("---------------------")
    # for d in dp :
    #     print(*d)
    # print("---------------------")

    for i in range(3) :
        if i != j :
            ans = min(ans, dp[N - 1][i])

print(ans)