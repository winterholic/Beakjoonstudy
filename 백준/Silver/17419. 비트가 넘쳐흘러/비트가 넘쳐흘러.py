N = int(input())
binary_data = input()
binary_list = list(binary_data)
# print(binary_list)

cnt = 0

for i in range(len(binary_list) - 1, - 1, - 1) :
    if binary_list[i] == '1' :
        cnt += 1

# ans = ''.join(binary_list)
# print(ans)
print(cnt)