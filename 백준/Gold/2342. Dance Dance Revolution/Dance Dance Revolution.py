command = list(map(int, input().split()))

command.pop()
N = len(command)

# print(command)
# print(N)

dp = [[[400001] * 5 for _ in range(5)] for _ in range(N + 1)] # 0 : 왼발 1 : 오른발
dp[-1][0][0] = 0

#중앙발이 움직이면 2의 힘 , 대각선이동 3의힘, 반대이동 4의 힘, 같은지점 1, 같은 수 - 같은 수도 짝수
def cal_prime(fr, fo) :
    if fr == 0 :
        if fo == 0 :
            return 0
        else :
            return 2
    elif abs(fr - fo) % 2 == 1 :
        return 3
    elif fr == fo :
        return 1
    else :
        return 4

for i in range(N) :
    for j in range(5) :
        for k in range(5) :
            dp[i][command[i]][j] = min(dp[i][command[i]][j], dp[i - 1][k][j] + cal_prime(k, command[i]))

    for j in range(5) :
        for k in range(5) :
            dp[i][j][command[i]] = min(dp[i][j][command[i]], dp[i - 1][j][k] + cal_prime(k, command[i]))


ans = 400001
for i in range(5) :
    for j in range(5) :
        if(dp[N - 1][i][j] < ans) :
            ans = dp[N - 1][i][j]

print(ans)
# print(dp[N - 1])