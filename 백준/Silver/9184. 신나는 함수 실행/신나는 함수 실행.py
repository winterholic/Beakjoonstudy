import sys
input = sys.stdin.readline

dp = [[[0] * 21 for _ in range(21)]for _ in range(21)]

def jinxfunction(a, b, c) :
    if(a <= 0 or b <= 0 or c <= 0) :
        return 1
    if (a > 20 or b > 20 or c > 20) :
        return jinxfunction(20, 20, 20)
    if dp[a][b][c] :
        return dp[a][b][c]
    if (a < b and b < c) :
        dp[a][b][c] = jinxfunction(a, b, c - 1) + jinxfunction(a, b - 1, c - 1) - jinxfunction(a, b - 1, c)
        return dp[a][b][c]
    dp[a][b][c] = jinxfunction(a - 1, b, c) + jinxfunction(a - 1, b - 1, c) + jinxfunction(a - 1, b, c - 1) - jinxfunction(a - 1, b - 1, c - 1)
    return dp[a][b][c]

while(True) :
    a, b, c = map(int, input().split())
    if (a == -1) and (b == -1) and (c == -1) :
        break
    else :
        ans = ''
        ans += "w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(jinxfunction(a, b, c))
        print(ans)