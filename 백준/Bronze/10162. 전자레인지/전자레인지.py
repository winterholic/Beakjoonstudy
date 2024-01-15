N = int(input())

electro = [300, 60, 10]
answer = []

if (N % 10 != 0) :
    print(-1)
else :
    for elec in electro :
        if (N >= elec) :
            num = N // elec
            answer.append(num)
            N -= (num * elec)
        else :
            answer.append(0)
    for ans in answer :
        print(ans, end = " ")