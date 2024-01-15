import sys
input = sys.stdin.readline

N = int(input())

score = []
score.append(0)
for i in range(1, N + 1) : # 동전 종류 입력받기
    score.append(int(input()))

dp = [0] * (N + 1)

dp[0] = 0
dp[1] = score[1]

for i in range(2, N + 1) : # 1부터 k까지
    dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])

print(dp[N])