a = int(input())
dp = [0] * max(4, a + 1)
dp[0] = -1
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, a + 1) :
    if(i % 3 == 0 and i % 2 == 0) :
        new_data = min(dp[i//2], dp[i//3], dp[i - 1]) + 1
    elif(i % 3 == 0 and i % 2 != 0) :
        new_data = min(dp[i//3], dp[i - 1]) + 1
    elif(i % 2 == 0 and i % 3 != 0) :
        new_data = min(dp[i//2], dp[i - 1]) + 1
    else :
        new_data = dp[i - 1] + 1
    dp[i] = new_data

#for i in range(1, a + 1) :
    #print(i, ':', dp[i])

print(dp[a])