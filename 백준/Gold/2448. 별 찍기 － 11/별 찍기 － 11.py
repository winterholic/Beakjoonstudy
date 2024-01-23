N = int(input())

star = [[' '] * (2 * N) for _ in range(N)]

def drawingstar(i, j, cursize) :
    if(cursize == 3) :
        star[i][j] = "*"
        star[i + 1][j - 1] = "*"
        star[i + 1][j + 1] = "*"
        for k in range(-2, 3) :
            star[i + 2][j - k] = "*"
    
    else :
        recursionsize = cursize // 2
        drawingstar(i, j, recursionsize)
        drawingstar(i + recursionsize, j - recursionsize, recursionsize)
        drawingstar(i + recursionsize, j + recursionsize, recursionsize)

drawingstar(0, N - 1, N)

"""for i in range(N) :
    for j in range(2 * N) :
        print(star[i][j], end = "")
    print()"""

for s in star :
    print("".join(s))