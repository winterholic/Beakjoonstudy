import sys
input = sys.stdin.readline

def DFS(start, numbers) :
    if len(numbers) == M :
        for number in numbers :
            print(number, end = " ")
        print()
        return
    
    for i in range(start, N) :
        
        numbers.append(sorted_array[i])
        DFS(i, numbers)
        numbers.pop()

N, M = map(int, input().split())

# 숫자 입력 받아 리스트에 저장
array = list(map(int, input().split()))
sorted_array = sorted(array)

numbers = []
DFS(0, numbers)