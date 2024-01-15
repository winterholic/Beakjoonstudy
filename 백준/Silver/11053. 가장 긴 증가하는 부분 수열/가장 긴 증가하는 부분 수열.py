import sys
input = sys.stdin.readline

N = int(input())

number = []
number.append(0)

# 여러 숫자를 한 줄로 입력받아 배열에 저장
number.extend(map(int, input().split()))

dp = [1] * (N + 1)

for i in range(1, N + 1) :
    for j in range(1, i) : 
        if number[i] > number[j] :
            dp[i] = max(dp[i], dp[j] + 1)
            #print('dd')

#print(dp)
#print(number)
print(max(dp))