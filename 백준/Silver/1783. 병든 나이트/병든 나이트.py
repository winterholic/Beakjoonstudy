N, M = map(int, input().split())
ans = 0

if(N == 1) :
    ans = 1
elif(N == 2) :
    ans = min(4, ((M - 1) // 2) + 1)
elif(M < 7) :
    ans = min(4, M)
else :
    ans = (2 + (M - 5)) + 1

print(ans)