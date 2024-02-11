import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for i in range(T) :
    A = input()
    B = int(input())
    my_list = input()
    C = deque(eval(my_list))

    numR = 0
    flag = 1

    #print(':', A)

    for a in A :
        if(numR % 2 == 0) :
            if(a == 'R') :
                #print('1R')
                numR += 1
            elif(a == 'D') :
                if(len(C) > 0) :
                    #print('1D')
                    C.popleft()
                else :
                    print('error')
                    flag = 0
                    break
        else :
            if(a == 'R') :
                #print('2R')
                numR += 1
            elif(a == 'D') :
                if(len(C) > 0) :
                    #print('2D')
                    C.pop()
                else :
                    print('error')
                    flag = 0
                    break

    if(numR % 2 == 1) :
        C.reverse()

    if(flag == 1) :
        print('[', end = "")
        for i in range(len(C)) :
            if (i != len(C) - 1) :
                print(C[i], end = ",")
            else :
                print(C[i], end = "")
        print(']')


"""C = input()
my_list = eval(C)
for ml in my_list :
    print(ml, end = " ")"""