#import sys
#input = sys.stdin.readline
from collections import deque

N = int(input())
numbers = list(map(int, input().split()))

arr = [0]

for number in numbers :
    if number > arr[len(arr) - 1] :
        #print(number, arr[len(arr) - 1])
        arr.append(number)
    else :
        left = 0
        right = len(arr)

        while left < right :
            mid = (right + left) // 2
            #print(number ,mid, left, right)
            if(arr[mid] < number) :
                left = mid + 1
            else :
                right = mid
        arr[right] = number

arr.pop(0)
#print(arr)
print(len(arr))