import sys
input = sys.stdin.readline

def DFS(numbers) :
    if len(numbers) == M :
        for number in numbers :
            print(number, end = " ")
        print()
        return
    
    for i in range(1, N + 1) :
        
        numbers.append(i)
        DFS(numbers)
        numbers.pop()

N, M = map(int, input().split())

numbers = []
DFS(numbers)