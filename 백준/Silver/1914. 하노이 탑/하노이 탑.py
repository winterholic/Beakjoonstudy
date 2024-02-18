N = int(input())

cnt = 0

hanoi_data = []

def Hanoi(N, s, temp, e) :
    if(N == 1) :
        print(s, e)
        return
    else :
        Hanoi(N - 1, s, e, temp)
        print(s, e)
        Hanoi(N - 1, temp, s, e)

print(pow(2, N) - 1)
if N <= 20 :
    Hanoi(N, 1, 2 ,3)