import sys
input = sys.stdin.readline

def DFS(numbers) :
    if len(numbers) == M :
        for number in numbers :
            print(number, end = " ")
        print()
        return
    
    for i in range(0, N) :
        if sorted_array[i] in numbers :
            continue
        
        numbers.append(sorted_array[i])
        DFS(numbers)
        numbers.pop()

N, M = map(int, input().split())

# 숫자 입력 받아 리스트에 저장
array = list(map(int, input().split()))
sorted_array = sorted(array)

numbers = []
DFS(numbers)