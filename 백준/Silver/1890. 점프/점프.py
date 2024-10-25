import sys
input = sys.stdin.readline

N = int(input())

game_board = []

for i in range(N) :
    game_board.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N) :
    for j in range(N) :
        cost = game_board[i][j]
        if cost == 0 :
            continue
        if i + cost < N :
            dp[i + cost][j] += dp[i][j]
        if j + cost < N :
            dp[i][j + cost] += dp[i][j]


# print(dp)
print(dp[N - 1][N - 1])