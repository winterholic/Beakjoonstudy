N = int(input())

for i in range(1, 1000001) :
    data = sum(map(int, str(i)))
    datasum = i + data
    if datasum == N :
        print(i)
        break
    if i == N :
        print(0)