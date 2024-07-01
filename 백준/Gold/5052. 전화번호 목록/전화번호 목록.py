import sys
input = sys.stdin.readline

T = int(input())

def making_tree(temp_tree, try_list):
    global flag
    if try_list[0] not in temp_tree:
        if len(try_list) == 1:
            temp_tree[try_list[0]] = [{}, 1]
        else:
            temp_tree[try_list[0]] = [{}, 0]
    else:
        # 현재 노드가 리프 노드이면 flag를 0으로 설정
        if temp_tree[try_list[0]][1] == 1:
            flag = 0
        if len(try_list) == 1 :
            flag = 0

    if len(try_list[1:]) != 0:
        making_tree(temp_tree[try_list[0]][0], try_list[1:])




for i in range(T) :
    N = int(input())
    number = []
    for j in range(N) :
        temp = list(input().rstrip())
        number.append(temp)

    number_dict = {}
    for j in range(N) :
        # print(number[j])
        flag = 1
        making_tree(number_dict, number[j])
        if flag == 0 :
            print("NO")
            break
    if flag == 1 :
        print("YES")
    # print(number_dict)
    # print("00000000000000000000000000000000__",flag)