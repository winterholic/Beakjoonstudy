import sys
import itertools
from copy import deepcopy
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = []

for i in range(N) :
    temp = list(map(int, input().split()))
    arr.append(temp)

try_list = []

for i in range(K) :
    temp = list(map(int, input().split()))
    try_list.append(temp)

def rotation(x, y, r, array) :
    for i in range(r) :
        fx = x - r + i
        fy = y - r + i
        ex = x + r - i
        ey = y + r - i
        temp = array[fx][fy]

        for k in range(0, 2 * (r - i)) :
            array[fx + k][fy] = array[fx + k + 1][fy]
        
        for k in range(0, 2 * (r - i)) :
            array[ex][fy + k] = array[ex][fy + k + 1]

        for k in range(0, 2 * (r - i)) :
            array[ex - k][ey] = array[ex - k - 1][ey]

        for k in range(0, 2 * (r - i)) :
            array[fx][ey - k] = array[fx][ey - k - 1]

        array[fx][fy + 1] = temp

"""for i in range(N) :
    for j in range(M) :
        print(arr[i][j], end = " ")
    print()"""

def generate_combinations(lst):
    result = []
    for perm in itertools.permutations(lst):
        result.append(list(perm))
    return result

def get_min_sum(array):
    min_sum = 1000000000
    for row in array:
        min_sum = min(min_sum, sum(row))
    return min_sum

# 예시: 요소의 개수가 3개인 리스트를 입력으로 받아 모든 순서의 조합을 생성
order_list = []
for i in range(len(try_list)) :
    order_list.append(i)
combinations = generate_combinations(order_list)
#print(combinations)

min_data = 1000000000

for i in range(len(combinations)) :
    copied_arr = deepcopy(arr)
    for j in range(len(combinations[i])) :
        x = try_list[combinations[i][j]][0] - 1
        y = try_list[combinations[i][j]][1] - 1
        r = try_list[combinations[i][j]][2]
        #print(x + 1 , y + 1, r)
        rotation(x, y, r, copied_arr)
    temp_min = get_min_sum(copied_arr)
    if(temp_min < min_data) :
        min_data = temp_min

print(min_data)