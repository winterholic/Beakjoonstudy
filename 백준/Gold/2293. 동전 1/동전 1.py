import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n과 k 입력

coins = [] # 동전의 종류를 저장할 리스트
for i in range(0, n) : # 동전 종류 입력받기
    coins.append(int(input()))

dp = [0] * (k + 1) # dp배열 초기값 0 입력
dp[0] = 1 #초기값 0으로 설정 코인이 1원이 있을때를 계산하기 위해서 0에는 0의 값이 담겨있어야한다.

#print(coins)

"""
for i in range(1, k + 1) : # 1부터 k까지
    for coin in coins : # 모든 coin으로 확인
        if i >= coin :
            dp[i] += dp[i - coin]
            print('cal', i, coin)
"""

for coin in coins :
    for i in range(1, k + 1) :
        if i >= coin :
            dp[i] += dp[i - coin]

#print(dp)
print(dp[k])