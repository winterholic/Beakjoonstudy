import sys
input = sys.stdin.readline

def DFS(start, numbers) :
    if len(numbers) == M :
        for number in numbers :
            print(number, end = " ")
        print()
        return
    
    for i in range(start, N + 1) :
        numbers.append(i)
        DFS(i, numbers)
        numbers.pop()

N, M = map(int, input().split())

numbers = []
DFS(1, numbers)