from collections import deque

N, K = map(int, input().split())
numbers = list(input())

stack = []

for i in range(N) :
    numbers[i] = int(numbers[i])

for i in range(N) :
    while stack :
        if(stack[-1] >= numbers[i] or K == 0) :
            break

        stack.pop()
        K -= 1

    stack.append(numbers[i])

if K == 0 :
    for s in stack :
        print(s, end = "")
else :
    for i in range(len(stack) - K) :
        print(stack[i], end = "")