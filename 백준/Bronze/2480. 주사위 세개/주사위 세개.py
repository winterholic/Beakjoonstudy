a, b, c = map(int, input().split())
if (a == b and b == c) :
    ans = 10000 + a * 1000
elif (a == b and b != c) :
    ans = 1000 + a * 100
elif (a == c and c != b) :
    ans = 1000 + a * 100
elif (b == c and c != a) :
    ans = 1000 + b * 100
elif (a != b and b != c and c != a) :
    if (a > b and a > c) :
        ans = a * 100
    elif (b > a and b > c) :
        ans = b * 100
    elif (c > a and c > b) :
        ans = c * 100
print(ans)