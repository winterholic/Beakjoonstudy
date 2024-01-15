import sys
input = sys.stdin.readline

N = int(input())

energy = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
sum_price = 0

for i in range (0, N - 1) :
    if min_price > price[i] :
        min_price = price[i]
    sum_price += min_price * energy[i]

print(sum_price)