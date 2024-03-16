import sys
sys.setrecursionlimit(10 ** 6)
import copy

N = int(input())

calorder = [' ', '+', '-']
    
def DFS(array, last) :
    if len(array) == last :
        temp = copy.deepcopy(array)
        callist.append(temp)
        return
    
    for i in range(3) :
        array.append(calorder[i])
        DFS(array, last)
        array.pop()

for i in range(N) :
    TC = int(input())
    callist = []
    #print(callist, TC - 1)
    DFS([], TC - 1)
    #print(callist)
    for c in callist :
        tempstr = ''
        for i in range(TC - 1) :
            if(i != TC - 2) :
                tempstr += str(i + 1) + c[i]
            else :
                tempstr += str(i + 1) + c[i] + str(i + 2)
        tempstr2 = tempstr.replace(' ', '')
        result = eval(tempstr2)
        if(result == 0) :
            print(tempstr)
    print()