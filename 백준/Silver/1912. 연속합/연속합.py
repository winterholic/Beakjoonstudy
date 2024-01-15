import sys
input = sys.stdin.readline

n = int(input())

number = []

# 여러 숫자를 한 줄로 입력받아 배열에 저장
number.extend(map(int, input().split()))

dp = [0] * n
dp[0] = number[0]

for i in range(1, n) :
    dp[i] = max(number[i], dp[i - 1] + number[i])

#print(dp)
print(max(dp))