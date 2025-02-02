N, X = map(int, input().split())

L = [0] * (N + 1)
P = [0] * (N + 1)

L[0] = 1
P[0] = 1

for i in range(1, N + 1):
    L[i] = 2 * L[i - 1] + 3
    P[i] = 2 * P[i - 1] + 1

# 레벨-1 버거는 'BPPPB', 레벨-2 버거는 'BBPPPBPBPPPBB', 레벨-3 버거는 'BBBPPPBPBPPPBBPBBPPPBPBPPPBBB' , 레벨-4 버거는 'BBBBPPPBPBPPPBBPBBPPPBPBPPPBBBPBBBPPPBPBPPPBBPBBPPPBPBPPPBBBB'

def func(n, x):
    if n == 0:  # 레벨 0 햄버거는 패티 1개만 존재
        return 1 if x > 0 else 0  # x가 0보다 크면 패티 1개, 아니면 패티 0개
    if x == 1: # 맨 위 빵은 패티가 없음
        return 0
    elif x <= 1 + L[n - 1]: # 맨 위 빵 이후, 첫 번째 레벨 n-1 햄버거의 일부를 먹은 경우
        return func(n - 1, x - 1) # 첫 번째 레벨 n-1 햄버거의 일부를 먹음
    elif x == 1 + L[n - 1] + 1: # 첫 번째 레벨 n-1 햄버거 전체와 중간 패티까지 먹은 경우
        return P[n - 1] + 1 # 첫 번째 레벨 n-1 햄버거 전체와 중간 패티까지 먹음
    elif x <= 1 + L[n - 1] + 1 + L[n - 1]: # 첫 번째 레벨 n-1 햄버거 + 중간 패티 + 두 번째 레벨 n-1 햄버거의 일부를 먹은 경우
        return P[n - 1] + 1 + func(n - 1, x - (L[n - 1] + 2)) # 두 번째 레벨 n-1 햄버거의 일부를 먹음
    else: # 햄버거 전체를 먹은 경우
        return P[n]

print(func(N, X))