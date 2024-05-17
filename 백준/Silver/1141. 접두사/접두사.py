import sys

stringX = []
N = int(input())

for i in range(N) :
    tempstr = input()
    tempstr = list(tempstr)
    stringX.append(tempstr)

stringX.sort(key = len)
ans = 0

#print(stringX)

for i in range(N) :
    flag = 0
    for j in range(i + 1, N) :
        stra = ''.join(stringX[i])
        strb = ''.join(stringX[j][0 : len(stra)])
        #print(stra, strb)
        if stra == strb : 
            flag = 1
            break
    if flag == 0 :
        ans += 1

print(ans)