import sys
input = sys.stdin.readline

N = int(input())

plan = []

for i in range(N) :
    plan.append(list(map(int, input().split())))

#print(plan)

dp = [0] * (N + 1)

for i in range(N) :
    for j in range(i + plan[i][0], N + 1) :
        dp[j] = max(dp[j], dp[i] + plan[i][1])

print(dp[N])