import sys
input = sys.stdin.readline

flowers = []
N = int(input())
for i in range(N) :
    sm, sd, fm, fd = map(int, input().split())
    flowers.append([sm * 100 + sd, fm * 100 + fd])

flowers.sort()

ending = 301
cnt = 0

while True :
    if (not flowers) or (ending > 1130) or (ending < flowers[0][0]):
        break

    temp = -1
    for i in range(len(flowers)) :
        if (flowers[0][0] <= ending) :
            temp = max(temp, flowers[0][1])
            flowers.pop(0)
        else :
            break
    
    ending = temp
    cnt += 1

if ending <= 1130 :
    cnt = 0
print(cnt)