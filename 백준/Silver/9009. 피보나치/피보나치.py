import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 51

dp[1] = 1

for i in range(2, 51) :
    dp[i] = dp[i - 1] + dp[i - 2]

# print(dp[50])

TK = []

for i in range(N) :
    TK.append(int(input()))

for tk in TK :
    anslist = []
    for i in range(50, 0, -1) :
        if(dp[i] <= tk) :
            anslist.append(dp[i])
            tk -= dp[i]

    anslist.sort() 
    for al in anslist :
        print(al, end = " ")

    print()
        

# for i in range(3, -1, -1) :
#     print(i)