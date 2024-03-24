from itertools import combinations
from collections import deque

def generate_combinations(A, B, nA, nB):
    result = []
    # A 배열에서 5개를 선택하는 조합 생성
    for comb_A in combinations(A, nA):
        # B 배열에서 2개를 선택하는 조합 생성
        for comb_B in combinations(B, nB):
            result.append(list(comb_B) + list(comb_A))
    return result

graph = []
for i in range(5) :
    temp = list(input())
    graph.append(temp)

#print(graph)

leelist = []
limlist = []

for i in range(5) :
    for j in range(5) :
        if(graph[i][j] == 'Y') :
            limlist.append((i, j))
        else :
            leelist.append((i, j))

list43 = generate_combinations(leelist, limlist, 4, 3)
list52 = generate_combinations(leelist, limlist, 5, 2)
list61 = generate_combinations(leelist, limlist, 6, 1)
list70 = generate_combinations(leelist, limlist, 7, 0)

#print(list43)

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# ans1 = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (3, 1)]
# ans2 = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]


def BFS(princesslist) :
    visited = [[0] * 5 for _ in range(5)]
    queue = deque()
    queue.append(princesslist[0])
    visited[princesslist[0][0]][princesslist[0][1]] = 1

    # flag1 = 1
    # flag2 = 1
    # for an in ans1 :
    #     if not an in princesslist :
    #         flag1 = 0

    # for an in ans2 :
    #     if not an in princesslist :
    #         flag2 = 0

    while queue :
        x, y = queue.popleft()

        for dir in direct :
            px = x + dir[0]
            py = y + dir[1]

            # if flag2 == 1 and x == 1 and y == 4 :
            #     print(px, py)

            if px < 0 or py < 0 or px >= 5 or py >= 5 :
                continue

            if visited[px][py] == 0 and (px, py) in princesslist :
                queue.append((px, py))
                visited[px][py] = visited[x][y] + 1

    # if flag1 == 1 or flag2 == 1 :
    #     for v in visited :
    #         print(*v)
    #     print()

    cnt = 0
    for i in range(5) :
        for j in range(5) :
            if(visited[i][j] != 0) :
                cnt += 1

    if(cnt == 7) :
        return 1
    else :
        return 0

listprincess = list43 + list52 + list61 + list70

ans = 0

for lp in listprincess :
    ans += BFS(lp)
    #print(*lp)

print(ans)