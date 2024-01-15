import sys
input = sys.stdin.readline

N = int(input())
minimal = 300

def DFS(current, index) :
    global minimal
    if current == N // 2 :
        case1 = 0
        case2 = 0
        for i in range(N) :
            for j in range(N) :
                if (visited[i] == 1) and (visited[j] == 1) :
                    case1 += start_link[i][j]
                elif (visited[i] == 0) and (visited[j] == 0) :
                    case2 += start_link[i][j]
        #print(minimal, case1, case2, "dd")
        minimal = min(minimal, abs(case1 - case2))
        #print(minimal)
        return
    
    for i in range(index, N) :
        if (visited[i] == 0) :
            #print(i)
            visited[i] = 1
            DFS(current + 1, i + 1)
            visited[i] = 0

start_link = [list(map(int, input().split())) for _ in range(N)]
#print(start_link)
visited = [0] * N
#print(visited)

DFS(0, 0)
print(minimal)