import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

number = []

while True :
    try :
        number.append(int(input()))
    except :
        break

#print(number)

def DFS(thislist) :
    lenl = len(thislist)
    if lenl == 0 :
        return  
    
    flag = 0
    mid = 0
    leftlist = []
    rightlist = []

    for i in range(1, lenl) :
        if thislist[i] > thislist[mid] :
            leftlist = thislist[1 : i]
            rightlist = thislist[i :]
            flag = 1
            break
    
    if flag == 0 :
        leftlist = thislist[1 :]

    DFS(leftlist)
    DFS(rightlist)
    print(thislist[mid])

DFS(number)