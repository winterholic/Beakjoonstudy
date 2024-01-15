a, b = map(int, input().split())

def isPelindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

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
    
Pelindrome_list = []

if (10000 >= b >= 1000) :
    b = 1000
if (1000000 >= b >= 100000) :
    b = 100000
if (b >= 10000000) :
    b = 10000000

for i in range(a, b + 1) :
    if(isPelindrome(i)) :
        Pelindrome_list.append(i)

for Pelindrome in Pelindrome_list :
    if(isdecimal(Pelindrome)) :
        print(Pelindrome)

print(-1)