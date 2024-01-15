import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = list(map(int, input().split()))

dp = [0] * (M + 1)
dp[0] = 1

sum = 0
ans = 0

for num in number :
    sum += num

    ans += dp[sum % M]
    #print(ans, sum, dp)
    dp[sum % M] += 1

#print(dp)
print(ans)