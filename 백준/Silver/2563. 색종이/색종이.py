arr = [[0] * 101 for _ in range(101)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            arr[j][k] = 1

print(sum(sum(line) for line in arr))