stringlist = []
turn = 1
while True :
    temp = input()
    if "-" in temp :
        break
    temp = list(temp)
    stack = []
    count = 0
    for t in temp :
        if t == "{" :
            stack.append(t)
        else :
            if stack :
                stack.pop()
            else :
                count += 1
                stack.append("{")
    count += len(stack) // 2
    ans = str(turn) + ". " + str(count)
    print(ans)
    turn += 1