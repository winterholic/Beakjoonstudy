import sys
sys.setrecursionlimit(10 ** 6)
from itertools import combinations

exinput = []
answer = []

game = list(combinations(range(0, 6), 2))

ans = 0

def DFS(results, depth):
    global ans
    if depth == 15:
        ans = 1
        for r in results :
            for j in range(3) :
                if(r[j] != 0) :
                    ans = 0
                    break
        return

    home, away = game[depth]
    for i in range(3):
        if results[home][i] > 0 and results[away][2 - i] > 0:
            results[home][i] -= 1
            results[away][2 - i] -= 1
            DFS(results, depth + 1)
            results[home][i] += 1
            results[away][2 - i] += 1

for i in range(4):
    w1, d1, l1, w2, d2, l2, w3, d3, l3, w4, d4, l4, w5, d5, l5, w6, d6, l6 = map(int, input().split())
    temp = [[w1, d1, l1], [w2, d2, l2], [w3, d3, l3], [w4, d4, l4], [w5, d5, l5], [w6, d6, l6]]
    exinput.append(temp)
    ans = 0
    DFS(temp, 0)
    answer.append(ans)

print(*answer)