N = int(input())

rooms = []

for i in range(N) :
    temp = list(map(int, input().split()))
    rooms.append(temp)

rooms.sort(key=lambda x: (x[1], x[0]))

ans = 0
time = 0

for room in rooms :
    if(room[0] >= time) :
        ans += 1
        time = room[1]

print(ans)