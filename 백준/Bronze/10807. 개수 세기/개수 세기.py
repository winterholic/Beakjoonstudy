N = int(input())

numbers = list(map(int,input().split()))

v = int(input())

cnt = 0

for number in numbers :
    if(number == v) :
        cnt += 1

print(cnt)