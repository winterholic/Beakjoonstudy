k = int(input())
dp = [[0] * 15 for _ in range(15)]

for i in range(0, 15) :
    for j in range (1, 15) :
        if(i == 0) :
            dp[i][j] = j
            #print(dp[i][j], end=" ")
        else :
            if(j == 1) :
                dp[i][j] = 1
                #print(dp[i][j], end=" ")
            else :
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                #print(dp[i][j], end=" ")
    #print('\n')

"""
for i in range(0, 15) :
    for j in range (1, 15) :
        print(dp[i][j], end = " ")
    print('\n')
"""

for i in range(0, k) :
    a = int(input())
    b = int(input())
    print(dp[a][b])