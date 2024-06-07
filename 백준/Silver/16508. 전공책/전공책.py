import copy

origin = input()
origin_list = list(origin)

N = int(input())

data = []
for i in range(N) :
    temp = input().split()
    value = int(temp[0])
    string = temp[1]
    data.append((value, string))

alphabet_list = [0] * 26

for alp in origin_list :
    idx = ord(alp) - ord('A')
    alphabet_list[idx] += 1

# print(alphabet_list)

ans = float('inf')

for i in range(1 << N) :
    temp_list = copy.copy(alphabet_list)
    thisbinary = bin(i)[2:].zfill(N)
    # print(thisbinary)
    flag = 1
    sum = 0
    for j in range(len(thisbinary)) :
        if thisbinary[j] == '1' :
            sum += data[j][0]
            for k in range(len(data[j][1])) :
                idx = ord(data[j][1][k]) - ord('A')
                temp_list[idx] -= 1
    for tl in temp_list :
        if tl > 0 :
            flag = 0
    if flag == 1 :
        if sum < ans :
            ans = sum

if ans == float('inf'):
    ans = -1

print(ans)