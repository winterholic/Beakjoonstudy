# import sys
# input = sys.stdin.readline

# N = int(input())

# list2048 = []

# for _ in range(N) :
#     temp = list(map(int, input().split()))
#     list2048.append(temp)

# def up(arr) :
#     for i in range(N) :
#         bef = 0
#         for j in range(1, N) :
#             temp = arr[i][j]
#             arr[i][j] = 0
#             if arr[bef][j] == temp :
#                 arr[bef][j] *= 2
#                 bef += 1
#             elif arr[bef][j] == 0 :
#                 arr[bef][j] = temp
#             elif arr[bef][j] != temp and arr[bef][j] != 0 :
#                 bef += 1
#                 arr[bef][j] = temp
    
# def down(arr) :
#     for i in range(N) :
#         bef = N - 1
#         for j in range(N - 2, -1, -1) :
#             temp = arr[i][j]
#             arr[i][j] = 0
#             if arr[bef][j] == temp :
#                 arr[bef][j] *= 2
#                 bef -= 1
#             elif arr[bef][j] == 0 :
#                 arr[bef][j] = temp
#             elif arr[bef][j] != temp and arr[bef][j] != 0 :
#                 bef -= 1
#                 arr[bef][j] = temp

# def right(arr) :
#     for i in range(N) :
#         bef = N - 1
#         for j in range(N - 2, -1, -1) :
#             temp = arr[i][j]
#             arr[i][j] = 0
#             if arr[i][bef] == temp :
#                 arr[i][bef] *= 2
#                 bef -= 1
#             elif arr[i][bef] == 0 :
#                 arr[i][bef] = temp
#             elif arr[i][bef] != temp and arr[i][bef] != 0 :
#                 bef -= 1
#                 arr[i][bef] = temp

# def left(arr) :
#     for i in range(N) :
#         bef = 0
#         for j in range(1, N) :
#             temp = arr[i][j]
#             arr[i][j] = 0
#             if arr[i][bef] == temp :
#                 arr[i][bef] *= 2
#                 bef += 1
#             elif arr[i][bef] == 0 :
#                 arr[i][bef] = temp
#             elif arr[i][bef] != temp and arr[i][bef] != 0 :
#                 bef += 1
#                 arr[i][bef] = temp

# def DFS(arr, times) :
#     if times == 5 :
#         return max(arr)

import sys
input = sys.stdin.readline

N = int(input())

list2048 = []

for _ in range(N):
    temp = list(map(int, input().split()))
    list2048.append(temp)

dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 x 좌표 변화량
dy = [0, 0, -1, 1]  # 상하좌우 이동을 위한 y 좌표 변화량

def move(direction, arr):
    if direction == 0:  # 위로 이동
        for j in range(N):
            stack = []
            for i in range(N):
                if arr[i][j] != 0:
                    stack.append(arr[i][j])
                    arr[i][j] = 0
            idx = 0
            for num in stack:
                if not arr[idx][j]:
                    arr[idx][j] = num
                elif arr[idx][j] == num:
                    arr[idx][j] *= 2
                    idx += 1
                else:
                    idx += 1
                    arr[idx][j] = num
    elif direction == 1:  # 아래로 이동
        for j in range(N):
            stack = []
            for i in range(N - 1, -1, -1):
                if arr[i][j] != 0:
                    stack.append(arr[i][j])
                    arr[i][j] = 0
            idx = N - 1
            for num in stack:
                if not arr[idx][j]:
                    arr[idx][j] = num
                elif arr[idx][j] == num:
                    arr[idx][j] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    arr[idx][j] = num
    elif direction == 2:  # 왼쪽으로 이동
        for i in range(N):
            stack = []
            for j in range(N):
                if arr[i][j] != 0:
                    stack.append(arr[i][j])
                    arr[i][j] = 0
            idx = 0
            for num in stack:
                if not arr[i][idx]:
                    arr[i][idx] = num
                elif arr[i][idx] == num:
                    arr[i][idx] *= 2
                    idx += 1
                else:
                    idx += 1
                    arr[i][idx] = num
    elif direction == 3:  # 오른쪽으로 이동
        for i in range(N):
            stack = []
            for j in range(N - 1, -1, -1):
                if arr[i][j] != 0:
                    stack.append(arr[i][j])
                    arr[i][j] = 0
            idx = N - 1
            for num in stack:
                if not arr[i][idx]:
                    arr[i][idx] = num
                elif arr[i][idx] == num:
                    arr[i][idx] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    arr[i][idx] = num

def DFS(arr, times):
    if times == 5:
        return max(map(max, arr))

    max_result = 0
    for direction in range(4):  # 상하좌우 이동 시도
        new_arr = [row[:] for row in arr]  # 복사본 생성
        move(direction, new_arr)  # 이동
        max_result = max(max_result, DFS(new_arr, times + 1))  # 재귀적으로 DFS 호출
    return max_result

result = DFS(list2048, 0)
print(result)