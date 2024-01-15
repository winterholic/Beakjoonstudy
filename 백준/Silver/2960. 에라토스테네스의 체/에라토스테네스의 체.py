N, K = map(int, input().split())

numbers = []

cnt = 0

for i in range (N + 1) :
    numbers.append(True)

numbers[0] = False
numbers[1] = False

flag = 1

for i in range(2, N + 1) :
    if(flag == 0) :
        break
    for j in range(i, N + 1) :
        if(numbers[j] == True and j % i == 0) :
            numbers[j] = False
            cnt += 1
            if(cnt == K) :
                print(j)
                flag = 0
                break

#print(numbers)