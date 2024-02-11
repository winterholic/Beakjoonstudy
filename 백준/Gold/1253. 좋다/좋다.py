#import sys
#input = sys.stdin.readline
from collections import deque

N = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)

cnt = 0

for i in range(N) :
    ans = numbers[i]
    s = 0
    e = len(numbers) - 1

    while (s < e) :
        if numbers[s] + numbers[e] == ans :
            if(s != i and e != i) :
                cnt += 1
                break
            else :
                if(s == i) :
                    s += 1
                elif(e == i) :
                    e -= 1

        elif numbers[s] + numbers[e] < ans :
            s += 1

        elif numbers[s] + numbers[e] > ans :
            e -= 1

print(cnt)