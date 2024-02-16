#import sys
#input = sys.stdin.readline
from collections import deque

N = int(input())
numbers = list(map(int, input().split()))

arr = [0]

for number in numbers :
    if number > arr[len(arr) - 1] :
        #print("case1", number, arr[len(arr) - 1], arr)
        arr.append(number)
    else :
        left = 0
        right = len(arr) - 1
        mini = 1000000000

        while left <= right :
            mid = (right + left) // 2
            #print("case2", number ,mid, left, right, arr)
            if(arr[mid] >= number) :
                mini = min(mid, mini)
                right = mid - 1
            else :
                left = mid + 1
        arr[mini] = number

arr.pop(0)
#print(arr)
print(len(arr))