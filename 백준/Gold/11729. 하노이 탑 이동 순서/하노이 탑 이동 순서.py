N = int(input())

cnt = 0

hanoi_data = []

def Hanoi(N, s, temp, e) :
    if(N == 1) :
        hanoi_data.append((s, e))
        return
    else :
        Hanoi(N - 1, s, e, temp)
        hanoi_data.append((s, e))
        Hanoi(N - 1, temp, s, e)


Hanoi(N, 1, 2 ,3)
print(len(hanoi_data))
for i in range(len(hanoi_data)) :
    print(hanoi_data[i][0], hanoi_data[i][1])