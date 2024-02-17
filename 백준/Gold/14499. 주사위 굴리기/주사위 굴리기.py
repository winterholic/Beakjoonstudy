N, M, x, y, K = map(int, input().split())
#print(N, M, x, y, K)

mapdata = []

for _ in range(N) :
    temp = list(map(int, input().split()))
    mapdata.append(temp)

commend = list(map(int, input().split()))
#print(commend)

dice = [0, 0, 0, 0, 0, 0]
direct = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]

dice = [0, 0, 0, 0, 0, 0]

#print(mapdata)

px = x
py = y

for c in commend :
    tempx = px
    tempy = py
    px += direct[c][0]
    py += direct[c][1]

    if px < 0 or py < 0 or px >= N or py >= M :
        px = tempx
        py = tempy
        continue

    if(c == 1) :
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]

    elif(c == 2) :
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]

    elif(c == 3) :
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]

    elif(c == 4) :
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

    if mapdata[px][py] == 0 :
        mapdata[px][py] = dice[5]
    else :
        dice[5] = mapdata[px][py]
        mapdata[px][py] = 0

    print(dice[0])