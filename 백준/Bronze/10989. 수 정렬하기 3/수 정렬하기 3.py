import sys
input = sys.stdin.readline

N = int(input())

numbers = [0] * 10001

for i in range(N) :
    data = int(input())
    numbers[data] += 1

for i in range(1, 10001) :
    thisnum = numbers[i]
    if thisnum > 0 :
        for j in range(0, thisnum) :
            print(i)