import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp1 = [1] * N
dp2 = [1] * N

for i in range(N) :
    for j in range(i) :
        if (numbers[j] < numbers[i]) :
            dp1[i] = max(dp1[j] + 1, dp1[i])

numbers.reverse()

for i in range(N) :
    for j in range(i) :
        if(numbers[j] < numbers[i]) :
            dp2[i] = max(dp2[j] + 1, dp2[i])

dp2.reverse()

#print(dp1)
#print(dp2)

ans = 0

for i in range(N) :
    ans = max(ans, dp1[i] + dp2[i])

print(ans - 1)