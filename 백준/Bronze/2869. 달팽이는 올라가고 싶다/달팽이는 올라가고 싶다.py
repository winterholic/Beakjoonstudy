A, B, V = map(int, input().split())

curr = 0
day = 0

day = (V - A) / (A - B) + 1

if day == int(day) :
    print(int(day))
else :
    print(int(day) + 1)