N = int(input())

ans = 1
point = 1

while N > point :
    point += 6 * ans
    ans += 1
    
print(ans)