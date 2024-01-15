import sys
input = sys.stdin.readline

n = int(input())

n = 1000 - n

moneys = [500, 100, 50, 10, 5, 1]

count = 0

for money in moneys :
    while(n >= money) :
        n = n - money
        #print(money)
        count += 1

print(count)