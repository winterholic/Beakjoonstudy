import sys
input = sys.stdin.readline

N = int(input())

dp = [1] * 1000001
ans = [1] * 1000001

for i in range (2, 1000001) :
    j = 1
    while True :
        if (i * j > 1000000) :
            break
        dp[i * j] += i
        j += 1
    
for i in range(1, 1000001) :
    ans[i] = ans[i - 1] + dp[i]

for i in range (N) :
    number = int(input())
    print(ans[number] - 1)