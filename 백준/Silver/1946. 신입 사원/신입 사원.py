T = int(input())

for i in range(T) :
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank = sorted(rank)
    ans = 1
    temp = 0
    for j in range(N) :
        if rank[j][1] < rank[temp][1] :
            temp = j
            ans += 1

    print(ans)