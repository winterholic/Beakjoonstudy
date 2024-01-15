A, B = map(int, input().split())

count = 0

while(B > A) :
    if(B % 10 == 1) :
        count += 1
        B = B // 10
        #print(B)
        continue
    count += 1
    B = B / 2
    #print(B)

if (B == A) :
    print(count + 1)
else :
    print(-1)