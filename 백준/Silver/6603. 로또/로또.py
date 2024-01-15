import sys
input = sys.stdin.readline

def DFS(depth, index, numbers, parts) :
    if len(parts) == 6 :
        for part in parts :
            print(part, end = " ")
        print()
        return
    
    for i in range(index, numbers_len) :
        parts.append(numbers[i])
        DFS(depth + 1, i + 1, numbers, parts)
        parts.pop()
        

while True :
    temp = list(map(int, input().split()))
    numbers_len = temp[0]
    numbers = temp[1:]
    if (numbers_len == 0) :
        break
    parts = []
    DFS(0, 0, numbers, parts)
    print()