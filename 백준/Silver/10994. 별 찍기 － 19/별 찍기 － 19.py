N = int(input())

star = [[' '] * (1 + (4 * (N - 1))) for _ in range((1 + (4 * (N - 1))))]

cx = 2 * (N - 1)
cy = 2 * (N - 1)

star[cx][cy] = '*'

def drawingstar(i) :
    if(i == 0) :
        #print("finish")
        return
    else :
        #print("ddddd")
        for k in range(cx - (i * 2), cx + (i * 2) + 1):
            star[cy + (i * 2)][k] = '*'
            star[cy - (i * 2)][k] = '*'
        for k in range(cy - (i * 2), cy + (i * 2) + 1) :
            star[k][cx + (i * 2)] = '*'
            star[k][cx - (i * 2)] = '*'
        drawingstar(i - 1)

drawingstar(N - 1)

#print(star)

for s in star :
    print("".join(s))