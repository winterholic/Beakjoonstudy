N = int(input())

ans = 0
row = [0] * N

def check(index) :
    for i in range(index) :
        if ((row[i] == row[index]) or (abs(index - i) == abs(row[index] - row[i]))) :
            return False
    return True

def DFS(index) :
    global ans
    if index == N :
        ans += 1
        return
    
    for i in range(N) :
        row[index] = i
        if check(index) :
            DFS(index + 1)

DFS(0)
print(ans)