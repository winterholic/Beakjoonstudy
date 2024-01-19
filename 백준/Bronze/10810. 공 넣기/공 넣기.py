N, M = map(int, input().split())

bucket = [0] * (N + 1)

for x1 in range(M) :
    i, j, k = map(int, input().split())
    for x2 in range(i, j + 1) :
        bucket[x2] = k
            

for i in range(1, N + 1) :
    print(bucket[i], end = " ")