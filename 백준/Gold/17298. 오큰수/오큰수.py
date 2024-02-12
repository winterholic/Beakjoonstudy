import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
stack = []

stack.append(0)

result = [-1] * N

for i in range(len(numbers)) :
    while stack :
        if(numbers[stack[-1]] >= numbers[i]) :
            break

        res_index = stack.pop()
        result[res_index] = numbers[i]

    stack.append(i)

stack.pop(0)

for i in range(N) :
    print(result[i], end = " ")