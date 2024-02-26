N = int(input())

x, y = 0, 1

N = N % (15 * 100000)
#피사노 주기

for i in range(N) :
    x, y = y % 1000000, (x + y) % 1000000

print(x)