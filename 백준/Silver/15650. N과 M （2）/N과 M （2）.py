import sys
input = sys.stdin.readline

def DFS(start, numbers) :
    if len(numbers) == M :
        for number in numbers :
            print(number, end = " ")
        print()
        return
    
    for i in range(start, N + 1) :
        if i in numbers :
            continue
        
        numbers.append(i)
        
        DFS(i + 1, numbers)
        numbers.pop()

N, M = map(int, input().split())

numbers = []
DFS(1, numbers)