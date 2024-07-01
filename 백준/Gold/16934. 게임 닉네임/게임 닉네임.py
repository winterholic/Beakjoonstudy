import sys
input = sys.stdin.readline

N = int(input())

try_try = []

for i in range(N):
    temp = input().strip()
    try_try.append(temp)

# print(try_try)

tree = {}

def making_tree(temp_tree, try_list, alias):
    global flag
    if try_list[0] not in temp_tree :
        if flag == 1 :
            alias.append(try_list[0])
            print(''.join(alias))
        flag = 0
        temp_tree[try_list[0]] = [{}, 0]
        if len(try_list) == 1 :
            temp_tree[try_list[0]][1] += 1
    else:
        if len(try_list) == 1 :
            temp_tree[try_list[0]][1] += 1
        if len(try_list) == 1 and flag == 1 : 
            alias.append(try_list[0])
            if temp_tree[try_list[0]][1] != 1:
                alias.append(str(temp_tree[try_list[0]][1]))
            print(''.join(alias))

    if len(try_list[1:]) != 0:
        alias.append(try_list[0])
        making_tree(temp_tree[try_list[0]][0], try_list[1:], alias)

for i in range(N):
    flag = 1
    making_tree(tree, try_try[i], [])

