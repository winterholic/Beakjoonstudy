N, K = map(int, input().split())

coins = []

for i in range(N) :
    coins.append(int(input()))

# coins = coins[::-1]
coins.reverse()


#print(coins)

count = 0

for coin in coins :
    if(K >= coin) :
        num = K // coin
        #print(coin, num)
        count += num
        K -= (num * coin)

print(count)