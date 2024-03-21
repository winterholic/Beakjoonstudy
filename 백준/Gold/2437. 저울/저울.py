N = int(input())

disturbance = list(map(int, input().split()))
disturbance.sort()

ans = 1

for i in range(N) :
    #print(ans)
    if ans < disturbance[i]:
        break

    ans += disturbance[i]

print(ans)