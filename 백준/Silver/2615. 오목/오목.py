import sys
input = sys.stdin.readline

board = []

for i in range(19) :
    temp = list(map(int, input().split()))
    board.append(temp)


"""print()
for i in range(19) :
    for j in range(19) :
        print(board[i][j], end = " ")
    print()"""

direct = [[0, 1], [1, 0], [1, 1], [-1, 1]]

for x in range(19) :
    for y in range(19) :
        if board[x][y] == 0 :
            continue
        data = board[x][y]
        for dir in direct :
            count = 1
            px = x + dir[0]
            py = y + dir[1]

            while True : 
                if(px < 0 or py < 0 or px >= 19 or py >= 19 or data != board[px][py]) :
                    break

                count += 1

                if count == 5 :
                    nx = px + dir[0]
                    ny = py + dir[1]
                    nx2 = x - dir[0]
                    ny2 = y - dir[1]
                    if(0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == data) :
                        break
                    if(0 <= nx2 < 19 and 0 <= ny2 < 19 and board[nx2][ny2] == data) :
                        break

                    print(data)
                    print(x + 1, y + 1)
                    sys.exit(0)

                px = px + dir[0]
                py = py + dir[1]

print(0)