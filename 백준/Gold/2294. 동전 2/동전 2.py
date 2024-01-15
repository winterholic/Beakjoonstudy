import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n과 k 입력

coins = [] # 동전의 종류를 저장할 리스트
for i in range(0, n) : # 동전 종류 입력받기
    coins.append(int(input()))

dp = [99999] * (k + 1) # dp배열 초기값은 값이 될 수 없는 높은 값 입력, 1일때 k개만큼 있을 수 있으므로 k가 최대 10000까지 가능하다.
dp[0] = 0 #초기값 0으로 설정 코인이 1원이 있을때를 계산하기 위해서 0에는 0의 값이 담겨있어야한다.

for i in range(1, k + 1) : # 1부터 k까지
    for coin in coins : # 모든 coin으로 확인
        if i < coin : # coin이 i보다 크면 coin으로 i를 만들 수 없기 때문에 값을 갱신하지 않는다.
            continue
        dp[i] = min(dp[i], dp[i - coin] + 1) # 값을 비교한다. 현재 dp배열에 저장된 값과 i - 코인의 가격의 dp배열에 저장된 값 + 1(코인의 가격을 더해줘야하기 때문)을 비교하여 더 작은값 선택

if dp[k] == 99999 :
    dp[k] = -1

print(dp[k])