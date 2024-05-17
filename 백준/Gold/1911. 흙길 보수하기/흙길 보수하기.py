import sys
input = sys.stdin.readline

N, L = map(int, input().split())

woong = []

for i in range(N) :
    a, b = map(int, input().split())
    woong.append((a, b))

woong.sort(key = lambda x : (x[0], x[1]))

lastloc = woong[0][0]

ans = 0

for wo in woong :
    if lastloc < wo[1] :
        if lastloc < wo[0] :
            lastloc = wo[0]
        length = (wo[1] - lastloc)
        cnt = length // L
        if length % L != 0 :
            cnt += 1
        lastloc += cnt * L
        #print(ans, cnt)
        ans += cnt

print(ans)