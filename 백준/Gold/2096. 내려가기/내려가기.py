import sys
input = sys.stdin.readline

N = int(input())

dp = list(map(int, input().rstrip().split()))
dp_max = dp
dp_min = dp

for i in range(1, N) :
    temp = list(map(int, input().rstrip().split()))
    dp_max = [max(dp_max[0] + temp[0], dp_max[1] + temp[0]), max(dp_max[0] + temp[1], dp_max[1] + temp[1], dp_max[2] + temp[1]), max(dp_max[1] + temp[2], dp_max[2] + temp[2])]
    dp_min = [min(dp_min[0] + temp[0], dp_min[1] + temp[0]), min(dp_min[0] + temp[1], dp_min[1] + temp[1], dp_min[2] + temp[1]), min(dp_min[1] + temp[2], dp_min[2] + temp[2])]

print(max(dp_max), min(dp_min))