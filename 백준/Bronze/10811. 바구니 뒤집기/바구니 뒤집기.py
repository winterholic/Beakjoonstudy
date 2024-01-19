N, M = map(int, input().split())

bucket = [0]

for i in range(1, N + 1) :
    bucket.append(i)

#print(bucket)

for x1 in range(M) :
    i, j = map(int, input().split())
    bucket[i : j + 1] = reversed(bucket[i : j + 1])
    #print(bucket)

for i in range(1, N + 1) :
    print(bucket[i], end = " ")