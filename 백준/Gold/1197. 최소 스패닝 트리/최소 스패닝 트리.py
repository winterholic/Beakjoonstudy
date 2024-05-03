import sys
input = sys.stdin.readline

N, M = map(int, input().split())

possible = []
edgelist = []

for _ in range(M) :
    a, b, c = map(int, input().split())
    possible.append((a - 1, b - 1, c))

possible.sort(key = lambda x : x[2])
#print(possible)

parent_set = [i for i in range(N)]
# print(parent_set)

def find_parent(node):
    if parent_set[node] == node:
        return node
    parent_set[node] = find_parent(parent_set[node])  # 경로 압축(Path Compression)을 통해 부모를 찾음
    return parent_set[node]

def Kruskal():
    for k in possible:
        node1 = k[0]
        node2 = k[1]
        weigh = k[2]
        parent1 = find_parent(node1)
        parent2 = find_parent(node2)
        if parent1 == parent2:  # 두 노드의 부모가 같으면 사이클이 발생하므로 무시
            continue
        edgelist.append((node1, node2, weigh))
        parent_set[parent2] = parent1  # 한 부모 아래로 합치기

Kruskal()

sum = 0
for el in edgelist :
    sum += el[2]

# print(possible)
# print(parent_set)
# print(edgelist)
print(sum)