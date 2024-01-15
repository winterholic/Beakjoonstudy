a, b = map(int, input().split())
c = int(input())
c+= b

while(c >= 60) :
    c -= 60
    a += 1

b = c
a = a % 24

print(a, b)