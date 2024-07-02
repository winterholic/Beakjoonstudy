import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

line = []
answer = {}

for i in range(N) :
    a, b = list(map(int, input().split()))
    answer[b] = [a, 0]
    line.append([a, b])

line.sort()

arr = [-1000000001]

ans = []

dp = [0] * (N)

for i in range(N) :
    if line[i][1] > arr[len(arr) - 1] :
        #print("case1", number, arr[len(arr) - 1], arr)
        arr.append(line[i][1])
        dp[i] = len(arr) - 1
    else :
        left = 0
        right = len(arr)

        while left < right :
            mid = (right + left) // 2
            #print("case2", number ,mid, left, right, arr)
            if(arr[mid] < line[i][1]) :
                left = mid + 1
            else :
                right = mid
        arr[right] = line[i][1]
        dp[i] = right

arr.pop(0)
#print(arr)
print(N - len(arr))
#print(dp)

targeti = max(dp)
i = max(dp)
j = N - 1
ans = []


while(i <= targeti and j >= 0) :
    # print("this : ", dp[j], i)
    if (dp[j] == i) :
        # ans.append(line[j][0])
        # print(line[j][1])
        answer[line[j][1]][1] = 1
        i -= 1
    j -= 1

# print(answer)

for i in range(len(ans) - 1, -1, -1) :
    print(ans[i], end = " ")

for i in answer :
    if answer[i][1] == 0 :
        print(answer[i][0])