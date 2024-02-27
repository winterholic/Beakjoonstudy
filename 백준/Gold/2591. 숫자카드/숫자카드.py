number = list(input())
numbers = []
for i in range(len(number)) :
    if(number[i] == '0') :
        temp = numbers.pop()
        numbers.append(temp * 10)
    else :
        numbers.append(int(number[i]))

N = len(numbers)
dp = [0] * N
dp[0] = 1

for i in range(1, N) :
    if (i == 1) :
        if((numbers[i - 1] < 3 and numbers[i] < 10) or (numbers[i - 1] == 3 and numbers[i] < 5)) : dp[1] = 2
        else : dp[1] = 1
    else :
        if((numbers[i - 1] < 3 and numbers[i] < 10) or (numbers[i - 1] == 3 and numbers[i] < 5)) : dp[i] = dp[i - 2] + dp[i - 1]
        else : dp[i] = dp[i - 1]
print(dp[-1])