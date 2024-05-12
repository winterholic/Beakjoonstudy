n, m = map(int, input().split())

subject = []

for i in range(n) :
    a, b = map(int, input().split())
    temp = list(map(int, input().split()))
    temp = sorted(temp, reverse=True)
    #print(temp)
    if (b > a) :
        b = 1
    else :
        b = temp[b - 1]
    subject.append(b)

# print(subject)

subject.sort()

# print(subject)

cnt = 0

for sub in subject :
    # print(m)
    if m == 0 or m < 0: 
        break
    m -= sub
    cnt += 1

if m < 0 :
    cnt -= 1

print(cnt)