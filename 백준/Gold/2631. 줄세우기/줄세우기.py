from collections import deque

N = int(input())

line = [0]

for i in range(1, N + 1) :
    line.append(int(input()))

cnt = 0

dp = [1] * (N + 1)

for i in range(1, N + 1) :
    for j in range(1, i) : 
        if line[i] > line[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))