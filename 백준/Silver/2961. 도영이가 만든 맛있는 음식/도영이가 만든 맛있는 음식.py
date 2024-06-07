N = int(input())
tasty = []
for i in range(N) :
    S, B = map(int, input().split())
    tasty.append((S, B))

ans = float('inf')

for i in range(1, 1 << N) :
    sour_tasty = 1
    bitter_tasty = 0
    thisbinary = bin(i)[2:].zfill(N)
    for j in range(len(thisbinary)) :
        if thisbinary[j] == '1' :
            sour_tasty *= tasty[j][0]
            bitter_tasty += tasty[j][1]
    diff = abs(sour_tasty - bitter_tasty)
    if ans > diff :
        ans = diff

print(ans)