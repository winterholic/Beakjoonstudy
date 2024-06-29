import sys
N = int(input())

try_try = []

for i in range(N) :
    temp = list(input().split())
    try_try.append(temp[1 :])

# print(try_try)

tree = {}

def making_tree(temp_tree, try_list) :
    if try_list[0] not in temp_tree :
        temp_tree[try_list[0]] = {}
    if len(try_list[1 :]) != 0 :
        making_tree(temp_tree[try_list[0]], try_list[1:])

for i in range(N) :
    making_tree(tree, try_try[i])

# print(tree)

def printing(dict, depth=0):
    for key in sorted(dict.keys()):
        print('--' * depth + key)
        printing(dict[key], depth + 1)

printing(tree)