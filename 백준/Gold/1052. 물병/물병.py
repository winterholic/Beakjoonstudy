N, K = map(int, input().split())

cnt = 0

while True :
    binary_representation = bin(N)[2:]
    count_of_ones = binary_representation.count('1')
    if count_of_ones <= K :
        break
    N += 1
    cnt += 1

print(cnt)