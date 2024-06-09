import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trains = [0] * (N + 1)

comm = []
for i in range(M) :
    temp = list(map(int, input().split()))
    comm.append(temp)

# print(comm)

for i in range(M) :
    if comm[i][0] == 1 :
        trains[comm[i][1]] |= (1 << (comm[i][2] - 1)) # idx번째 불켜기 T5 : " << n << "\n";
    elif comm[i][0] == 2 :
        trains[comm[i][1]] &= ~(1 << (comm[i][2] - 1)) # i번째 비트 끄기 n &= ~(1 << idx); // 1'1'11 -> 1'0'11 == 11
    elif comm[i][0] == 3 :
        trains[comm[i][1]] = trains[comm[i][1]] << 1
        # 20번째 자리에 사람이 있으면 하차시키기
        trains[comm[i][1]] &= ((1 << 20) - 1)
    elif comm[i][0] == 4 :
        trains[comm[i][1]] = trains[comm[i][1]] >> 1

# print(trains)

train_set = set()

for i in range(1, N + 1) :
    train_set.add(trains[i])

print(len(train_set))