N = int(input())

binary_representation = list(bin(N)[2:])
#print(binary_representation)

cnt = 0

for b in binary_representation :
    if b == '1' :
        cnt += 1

print(cnt)