N = int(input())
binary_representation = bin(N)[2:]  # "0b"를 제외한 부분만 가져옵니다.
# print(binary_representation)
binary_list = list(binary_representation)
# print(binary_list)
initial_number = 1
sum = 0
for i in range(len(binary_list) -1, -1, -1) :
    # print(binary_list[i], initial_number)
    if(binary_list[i] == '1') :
        sum += initial_number
    initial_number *= 3

print(sum)