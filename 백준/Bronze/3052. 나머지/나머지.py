numbers = {}

for i in range(1000) :
    numbers[i] = 0

for i in range(10) :
    N = int(input())
    numbers[N % 42] += 1

cnt = 0

for i in range(1000) :
    if(numbers[i] != 0) :
        cnt += 1

print(cnt)