N = int(input())

numbers = []

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

for i in range(N) :
    numbers.append(int(input()))

for number in numbers :
    for i in range(number // 2, 1, -1) :
        if (isdecimal(i)) :
            if (isdecimal(number - i)) :
                ans1 = i
                ans2 = number - i
                break
    print(ans1, ans2)