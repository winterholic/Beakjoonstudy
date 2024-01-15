N = int(input())

def isdecimal(num) :
    flag = 1
    limit = int(num ** 0.5)
    for j in range (2, limit + 1) :
        if (num % j == 0) :
            flag = 0
            break
    if flag == 1 :
        return True
    else :
        return False

decimal = []
decimal.append([0])
decimal.append([2, 3, 5, 7])

for i in range(2, 9) :
    temp = []
    for dec in decimal[i - 1] :
        tmp = dec * 10
        for j in range(1, 10) :
            new_tmp = tmp + j
            if (isdecimal(new_tmp)) :
                temp.append(new_tmp)
    decimal.append(temp)

for dec in decimal[N] :
    print(dec)