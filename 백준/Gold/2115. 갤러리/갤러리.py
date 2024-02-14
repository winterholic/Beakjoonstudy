import sys
#input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())

arr = []

tmp1 = ['X'] * (N + 2)

arr.append(tmp1)

for _ in range(M) :
    temp = deque(input())
    temp.append('X')
    temp.appendleft('X')
    temp = list(temp)
    arr.append(temp)

arr.append(tmp1)

#print(init_arr)

"""for i in range(M + 2) :
    for j in range(N + 2) :
        print(arr[i][j], end = " ")
    print()"""

i = 0
j = 0

cnt = 0

while(i <= M) :
    #print(i, j)
    j = 0
    while(j <= N) :
        #print(arr[i][j], arr[i + 1][j], arr[i][j + 1], arr[i + 1][j + 1])
        if(arr[i][j] == 'X' and arr[i][j + 1] == 'X' and arr[i + 1][j] == '.' and arr[i + 1][j + 1] == '.') :
            #print(i, j, arr[i][j], arr[i][j + 1], arr[i + 1][j], arr[i + 1][j + 1])
            cnt += 1
            j += 1
        if(arr[i][j] == '.' and arr[i][j + 1] == '.' and arr[i + 1][j] == 'X' and arr[i + 1][j + 1] == 'X') :
            #print(i, j, arr[i][j], arr[i][j + 1], arr[i + 1][j], arr[i + 1][j + 1])
            cnt += 1
            j += 1
        j += 1
    i += 1

i = 0
j = 0

#print("----------------------------------------------------")
        
while(i <= N) :
    #print(i, j)
    j = 0
    while(j <= M) :
        #print(arr[i][j], arr[i + 1][j], arr[i][j + 1], arr[i + 1][j + 1])
        if(arr[j][i] == 'X' and arr[j + 1][i] == 'X' and arr[j][i + 1] == '.' and arr[j + 1][i + 1] == '.') :
            #print(i, j, arr[i][j], arr[i + 1][j], arr[i][j + 1], arr[i + 1][j + 1])
            cnt += 1
            j += 1
        elif(arr[j][i] == '.' and arr[j + 1][i] == '.' and arr[j][i + 1] == 'X' and arr[j + 1][i + 1] == 'X') :
            #print(i, j, arr[i][j], arr[i + 1][j], arr[i][j + 1], arr[i + 1][j + 1])
            cnt += 1
            j += 1
        j += 1
    i += 1

print(cnt)