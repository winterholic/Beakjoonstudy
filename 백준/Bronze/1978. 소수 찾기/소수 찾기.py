N = int(input())

number = list(map(int, input().split()))

ans = 0

def check(num) :
    if(num == 0 or num == 1) :
        return False
    for i in range(2, num) :
        if(num % i == 0) :
            return False
    return True

for i in range(N) :
    if(check(number[i])) :
        ans += 1

print(ans)