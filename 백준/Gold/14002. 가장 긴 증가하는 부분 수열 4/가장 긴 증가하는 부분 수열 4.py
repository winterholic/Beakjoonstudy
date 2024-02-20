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
targeti = max(dp)
i = max(dp)
j = N
ans = []
while(i <= targeti and j >= 0) :
    if (dp[j] == i) :
        ans.append(number[j])
        i -= 1
    j -= 1
#print(number)
print(max(dp))
for i in range(len(ans) - 1, -1, -1) :
    print(ans[i], end = " ")