import sys
sudoku = []

for _ in range(9):
    row = list(map(int, input().split()))
    sudoku.append(row)

problem = []

def findproblem() :
    for i in range(9) :
        for j in range(9) :
            if(sudoku[i][j] == 0) :
                temp = []
                temp.append(i)
                temp.append(j)
                problem.append(temp)

def Row(check, line) :
    for i in range(9) :
        if (check == sudoku[line][i]) :
            return False
    return True

def Col(check, line) :
    for i in range(9) :
        if (check == sudoku[i][line]) :
            return False
    return True

def Rectangle(check, line1, line2) :
    x = line1 // 3 * 3
    y = line2 // 3 * 3
    for i in range(3) :
        for j in range(3) :
            if (check == sudoku[x + i][y + j]) :
                return False
    return True

def DFS(index) :
    if index == len(problem) :
        for i in range(9) :
            for j in range(9) :
                print(sudoku[i][j], end = " ")
            print()
        sys.exit()
        
    
    for i in range(1, 10) :
        line1 = problem[index][0]
        line2 = problem[index][1]

        if Row(i, line1) and Col(i, line2) and Rectangle(i, line1, line2) :
            sudoku[line1][line2] = i
            DFS(index + 1)
            sudoku[line1][line2] = 0

#print("--------------------------------------------")

findproblem()
DFS(0)