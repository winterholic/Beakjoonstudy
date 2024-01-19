N, M = map(int, input().split())

bucket = [0]

for i in range(1, N + 1) :
    bucket.append(i)

for x1 in range(M) :
    i, j = map(int, input().split())
    tmp = bucket[i]
    bucket[i] = bucket[j]
    bucket[j] = tmp

for i in range(1, N + 1) :
    print(bucket[i], end = " ")