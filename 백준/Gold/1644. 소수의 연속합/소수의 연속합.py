N = int(input())

arr = [True] * (N + 1)
arr[0] = False
arr[1] = False

decimal = []

for i in range(2, N + 1) :
    if arr[i] :
        decimal.append(i)
        for j in range(2 * i, N + 1, i) :
            arr[j] = False
        

cnt = 0
i = 0
j = 0

while j <= len(decimal) :
    summ = sum(decimal[i:j])
    if summ == N :
        cnt += 1
        j += 1
    elif summ < N :
        j += 1
    else :
        i += 1

print(cnt)