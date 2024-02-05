import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

array = []

for i in range(N) :
    temp = list(map(int, input().split()))
    array.append(temp)

#print(array)

for _ in range(R) :
    times = min(N, M) // 2
    for i in range(0, times) :
        x = i
        y = i
        temp = array[x][y]

        for j in range(i + 1, N - i) :
            x = j
            temp2 = array[x][y]
            array[x][y] = temp
            temp = temp2

        for j in range(i + 1, M - i) :
            y = j
            temp2 = array[x][y]
            array[x][y] = temp
            temp = temp2

        for j in range(i + 1, N - i) :
            x = N - j - 1
            temp2 = array[x][y]
            array[x][y] = temp
            temp = temp2

        for j in range(i + 1, M - i) :
            y = M - j - 1
            temp2 = array[x][y]
            array[x][y] = temp
            temp = temp2

for i in range(N) :
    for j in range(M) :
        print(array[i][j], end = " ")
    print()