originstring = [0] * 32
newstring = [0] * 32

N = int(input())
origin_number = N

index = 0
while N > 0 :
    originstring[index] = N % 2
    N = N // 2
    index += 1

for i in range(32) :
    if originstring[i] == 0 :
        newstring[i] = 1
    else :
        newstring[i] = 0

newstring[0] += 1

for i in range(31) :
    if newstring[i] == 2 :
        newstring[i] = 0
        newstring[i + 1] += 1

if(newstring[31] == 2) :
    newstring[31] = 0

diffcnt = 0

for i in range(32) :
    if originstring[i] != newstring[i] :
        diffcnt += 1


# print(originstring)
# print(newstring)
print(diffcnt)