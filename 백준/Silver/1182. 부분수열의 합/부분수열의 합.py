import sys
input = sys.stdin.readline

N, S = map(int, input().split())

# 숫자 입력 받아 리스트에 저장
numbers = list(map(int, input().split()))

count = 0

def DFS(start, sum) :
    global count
    if start == N :
        return
    sum += numbers[start]
    if sum == S :
        count += 1

    DFS(start + 1, sum)
    DFS(start + 1, sum - numbers[start])

DFS(0, 0)
print(count)