import sys
input = sys.stdin.readline

T = int(input())

for i in range(T) :
    x, y = map(int, input().split())
    diff = y - x

    ans = 0
    flag = 1
    flagp = 0

    while flagp < diff :
        ans += 1
        flagp += flag
        if ans % 2 == 0 :
            flag += 1

    print(ans)