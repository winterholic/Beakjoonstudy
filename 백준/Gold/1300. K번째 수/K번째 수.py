N = int(input())
K = int(input())

left = 1
right = K

ans = -1

while (left <= right) :
    mid = (left + right) // 2

    num = 0
    for i in range(1, N + 1) :
        num += min(mid // i, N)

    if (num >= K) :
        ans = mid
        right = mid - 1

    else :
        left = mid + 1
    
print(ans)