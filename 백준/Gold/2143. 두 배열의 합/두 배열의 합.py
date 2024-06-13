T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A_sum = []
B_sum = []

for i in range(N) :
    temp = A[i]
    A_sum.append(A[i])
    for j in range(i + 1, N) :
        temp += A[j]
        A_sum.append(temp)
for i in range(M) :
    temp = B[i]
    B_sum.append(B[i])
    for j in range(i + 1, M) :
        temp += B[j]
        B_sum.append(temp)

A_sum.sort()
B_sum.sort()
answer = 0

def binary_search_left(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def binary_search_right(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

for i in range(len(A_sum)) :
    l = binary_search_left(B_sum, T - A_sum[i])
    r = binary_search_right(B_sum, T - A_sum[i])
    answer += r - l

print(answer)
