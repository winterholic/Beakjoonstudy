N, S = map(int, input().split())

numbers = list(map(int, input().split()))

start = 0
end = 0
sum = 0
ans = 100001

while True :
    if sum >= S :
        ans = min(ans, end - start)
        sum -= numbers[start]
        start += 1
    elif end == N :
        break
    else :
        sum += numbers[end]
        end += 1

if ans == 100001 :
    print(0)
else :
    print(ans)