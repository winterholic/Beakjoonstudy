N = int(input())

star = [[' '] * (N) for _ in range(N)]

def drawingstar(i, j, cursize) :
    star[i][j] = '*'
    star[i][j + 1] = '*'
    star[i][j + 2] = '*'
    star[i + 1][j] = '*'
    star[i + 1][j + 1] = ' '
    star[i + 1][j + 2] = '*'
    star[i + 2][j] = '*'
    star[i + 2][j + 1] = '*'
    star[i + 2][j + 2] = '*'
    if(cursize == N) :
        return
    for l in range(3) :
        for k in range(3) :
            if(l == 1 and k == 1) :
                continue
            drawingstar(i + (l * cursize), j + (k * cursize), cursize * 3)
    
drawingstar(0, 0, 3)

for s in star :
    print("".join(s))