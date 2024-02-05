import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

array = []

for i in range(N) :
    temp = list(map(int, input().split()))
    array.append(temp)

#print(array)

times = min(N, M) // 2
times_list = []


for i in range(times) :
    norm = (N - 1 - (2 * i)) * 2 + (M - 1 - (2 * i)) * 2
    for j in range(R % norm) :
        temp = array[i][i]
        for k in range(1 + i, M - i) :
            array[i][k - 1] = array[i][k]

        for k in range(1 + i, N - i) :
            array[k - 1][M - 1 - i] = array[k][M - 1 - i]
        
        for k in range(1 + i, M - i) :
            array[N - 1 - i][M - k] = array[N - 1- i][M - 1 - k]

        for k in range(1 + i, N - i) :
            array[N - k][i] = array[N - 1 - k][i]

        array[1 + i][i] = temp

for i in range(N) :
    for j in range(M) :
        print(array[i][j], end = " ")
    print()