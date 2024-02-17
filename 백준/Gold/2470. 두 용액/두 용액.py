import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
numbers = sorted(numbers)

anss = 0
anse = len(numbers) - 1
ansdata = abs(numbers[anss] + numbers[anse])

s = 0
e = len(numbers) - 1

while(s < e) :
    sumdata = numbers[s] + numbers[e]

    if abs(sumdata) < ansdata :
        ansdata = abs(sumdata)
        anss = s
        anse = e
    
    if sumdata < 0 :
        s += 1
    elif sumdata > 0:
        e -= 1
    else :
        break

print(numbers[anss], numbers[anse])