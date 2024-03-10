import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
numbers = sorted(numbers)
#print(numbers)

ansp = 0
anss = 1
anse = N - 1
ansdata = 100000000000000001

for i in range(N - 2) :
    fp = i
    s = i + 1
    e = N - 1

    while(s < e) :
        sumdata = numbers[s] + numbers[e] + numbers[fp]

        if abs(sumdata) < abs(ansdata) :
            ansdata = abs(sumdata)
            ansp = fp
            anss = s
            anse = e
        
        if sumdata < 0 :
            s += 1
        elif sumdata > 0:
            e -= 1
        else :
            print(numbers[ansp], numbers[anss], numbers[anse])
            sys.exit()

print(numbers[ansp], numbers[anss], numbers[anse])