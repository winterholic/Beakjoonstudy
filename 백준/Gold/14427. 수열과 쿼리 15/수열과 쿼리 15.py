import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

# N = 10
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [[1000000001, 0] for _ in range(N * 4)]

#start : 시작인덱스 , end : 마지막인덱스 , index : 세그먼트 트리의 인덱스 (무조건 1부터 시작)
def init(start, end, index) :
    if start == end :
        #print(index)
        tree[index][0] = numbers[start]
        tree[index][1] = start
        return tree[index]
    mid = (start + end) // 2
    lnode = init(start, mid, index * 2)
    rnode = init(mid + 1, end, index * 2 + 1)
    lnode_data = lnode[0]
    lnode_index = lnode[1]
    rnode_data = rnode[0]
    rnode_index = rnode[1]
    if(lnode_data <= rnode_data) :
        tree[index] = [lnode_data, lnode_index]
    else :
        tree[index] = [rnode_data, rnode_index]
    return tree[index]

def printing_tree() :
    for t in tree:
        print(t)

init(0, N - 1, 1)
#printing_tree()

#start : 시작인덱스 , end : 마지막인덱스 , index : 세그먼트 트리의 인덱스 (무조건 1부터 시작), what : 구간합을 수정하고자하는 노드 , value : 수정할 값
def update(start, end, index, what, value):
    if what < start or what > end:
        return tree[index]

    if start == end:
        tree[index] = [value, what]
        return tree[index]

    mid = (start + end) // 2

    lnode = update(start, mid, index * 2, what, value)
    rnode = update(mid + 1, end, index * 2 + 1, what, value)

    lnode_data, lnode_index = lnode
    rnode_data, rnode_index = rnode

    if (lnode_data <= rnode_data):
        tree[index] = [lnode_data, lnode_index]
    else:
        tree[index] = [rnode_data, rnode_index]

    return tree[index]
    
M = int(input())
for _ in range(M) :
    number_query = list(map(int, input().split()))
    if number_query[0] == 2 :
        print(tree[1][1] + 1)
    else :
        update(0, N - 1, 1, number_query[1] - 1, number_query[2])
        #printing_tree()