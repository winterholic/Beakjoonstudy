import sys
input = sys.stdin.readline

N = int(input())

wine = []
wine.append(0)
for i in range(1, N + 1) : # 동전 종류 입력받기
    wine.append(int(input()))

dp = [0] * (N + 4)

dp[0] = 0
dp[1] = wine[1]
if N >= 2 :
    dp[2] = wine[1] + wine[2]
if N >= 3 :
    dp[3] = wine[3] + max(wine[1], wine[2])

for i in range(4, N + 1) : # 1부터 k까지
    dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i], dp[i - 4] + wine[i - 1] + wine[i])

#print(dp)
print(max(dp))