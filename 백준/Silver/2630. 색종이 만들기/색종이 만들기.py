N = int(input())

graph = []

for i in range(N) :
    temp = list(map(int, input().split()))
    graph.append(temp)

blue = 0
white = 0

def paper(x, y, N) :
    global blue
    global white
    color = graph[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N) :
            if color != graph[i][j] :
                paper(x, y, N // 2)
                paper(x, y + (N // 2) , N // 2)
                paper(x + (N // 2), y, N // 2)
                paper(x + (N // 2), y + (N // 2), N // 2)
                return
    if color == 0 :
        white += 1
    else :
        blue += 1

paper(0, 0, N)
print(white)
print(blue)