N, M = map(int, input().split())

numbers = list(map(int, input().split()))

ans = 0

for i in range(N - 2) :
    for j in range(i + 1, N - 1) :
        for k in range(j + 1, N) :
            if (numbers[i] + numbers[j] + numbers[k] <= M) :
                ans = max(ans, numbers[i] + numbers[j] + numbers[k])

print(ans)