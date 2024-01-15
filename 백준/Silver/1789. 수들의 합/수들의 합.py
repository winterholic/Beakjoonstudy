N = int(input())

cnt = 0
sum = 0

i = 1
while(True) :
    if (sum > N) :
        break
    sum += i
    #print(i, sum, end = " ")
    cnt += 1
    i += 1

#print()

print(cnt - 1)