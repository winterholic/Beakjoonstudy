N = int(input())

numbers = []
for i in range(N) :
    numbers.append(int(input()))

ans = 0
multi = []
plus = []

for i in range(0, N) :
    if (numbers[i] > 1) :
        multi.append(numbers[i])
    elif (numbers[i] == 1) :
        ans += 1
    else :
        plus.append(numbers[i])

multi = sorted(multi, reverse = True)
plus = sorted(plus)

for i in range(0, len(multi), 2) :
    if (i == len(multi) - 1) :
        ans += multi[i]
    else :
        ans += multi[i] * multi[i + 1]

for i in range(0, len(plus), 2) :
    if (i == len(plus) - 1) :
        ans += plus[i]
    else :
        ans += plus[i] * plus[i + 1]

print(ans)