#import sys
#input = sys.stdin.readline
from collections import deque

N = int(input())
numbers = list(map(int, input().split()))

arr = [-1000000001]

ans = []

dp = [0] * (N)

for i in range(len(numbers)) :
    if numbers[i] > arr[len(arr) - 1] :
        #print("case1", number, arr[len(arr) - 1], arr)
        arr.append(numbers[i])
        dp[i] = len(arr) - 1
    else :
        left = 0
        right = len(arr)

        while left < right :
            mid = (right + left) // 2
            #print("case2", number ,mid, left, right, arr)
            if(arr[mid] < numbers[i]) :
                left = mid + 1
            else :
                right = mid
        arr[right] = numbers[i]
        dp[i] = right

arr.pop(0)
#print(arr)
print(len(arr))
#print(dp)

targeti = max(dp)
i = max(dp)
j = N - 1
ans = []

while(i <= targeti and j >= 0) :
    if (dp[j] == i) :
        ans.append(numbers[j])
        i -= 1
    j -= 1

for i in range(len(ans) - 1, -1, -1) :
    print(ans[i], end = " ")