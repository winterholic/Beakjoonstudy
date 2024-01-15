a, b = map(int, input().split())
if(a == 0 and b < 45) :
    print(23,60 - (45 - b))
else :
    if(b < 45) :
        print(a - 1, 60 - (45 - b))
    else :
        print(a, b - 45)