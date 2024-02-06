from collections import deque

X = int(input())

mystring = list(input())

initstring = mystring

cycle = -1

for i in range(X) :
    temp = [0] * len(mystring)
    sp = 0
    ep = len(mystring) - 1
    for j in range(len(mystring)) :
        if(j % 2 == 0) :
            temp[sp] = mystring[j]
            sp += 1
        else :
            temp[ep] = mystring[j]
            ep -= 1
    mystring = temp
    if(initstring == mystring) :
        cycle = i + 1
        #print(cycle)
        break

if cycle == -1 :
    x = X
else :
    x = X % cycle

mystring = initstring

for i in range(x) :
    temp = [0] * len(mystring)
    sp = 0
    ep = len(mystring) - 1
    for j in range(len(mystring)) :
        if(j % 2 == 0) :
            temp[sp] = mystring[j]
            sp += 1
        else :
            temp[ep] = mystring[j]
            ep -= 1
    mystring = temp

print("".join(mystring))