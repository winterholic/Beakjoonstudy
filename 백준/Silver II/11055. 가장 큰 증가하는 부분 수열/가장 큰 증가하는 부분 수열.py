import sys
input = sys.stdin.readline

N = int(input())

number = list(map(int, input().split()))

dp = [1] * N

dp[0] = number[0]

for i in range(N) :
    for j in range(i) : 
        if number[i] > number[j] :
            dp[i] = max(dp[i], dp[j] + number[i])
        else :
            dp[i] = max(dp[i], number[i])

print(max(dp))