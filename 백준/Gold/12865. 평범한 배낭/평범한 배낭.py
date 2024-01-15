import sys
input = sys.stdin.readline

N , K = map(int, input().split())

bags = []

for _ in range(N):
    numbers = list(map(int, input().split()))
    bags.append(numbers)

"""# bag 출력
for row in bags:
    print(row)"""

dp = [0] * (K + 1)

dp[0] = 0

for bag in bags :
    for i in range (K, bag[0] - 1, -1) :
        dp[i] = max(dp[i], dp[i - bag[0]] + bag[1])

#print(dp)
print(dp[K])