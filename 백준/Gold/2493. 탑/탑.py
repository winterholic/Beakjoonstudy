N = int(input())
doran = list(map(int, input().split()))

stack = []
ans = [0] * N

for i in range(N - 1, -1, -1) :
    while stack and doran[i] > stack[-1][0] :
        target = stack.pop()
        ans[target[1]] = i + 1
    stack.append((doran[i], i))

for a in ans :
    print(a, end = " ")