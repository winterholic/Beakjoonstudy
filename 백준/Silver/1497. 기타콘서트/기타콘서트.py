N, M = map(int, input().split())

data = []

for i in range(N) :
    temp = input().split()
    data.append((temp[0], temp[1]))

ans = float('inf')
maxsong = 0

for i in range(1, 1 << N) :
    song_list = [False] * M
    thisbinary = bin(i)[2:].zfill(N)
    cnt = 0
    gcnt = 0
    for j in range(len(thisbinary)) :
        if thisbinary[j] == '1' :
            gcnt += 1
            for k in range(0, len(data[j][1])) :
                if data[j][1][k] == 'Y' :
                    song_list[k] = True
    for sl in song_list :
        if sl == True :
            cnt += 1
    # print(song_list, thisbinary, maxsong, cnt, gcnt)
    if cnt > maxsong :
        maxsong = cnt
        ans = gcnt
    elif cnt == maxsong :
        if gcnt < ans :
            ans = gcnt

if maxsong == 0 :
    ans = -1
print(ans)