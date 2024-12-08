import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

minus_book = []
plus_book = []

for pos in map(int, sys.stdin.readline().rstrip().split()):
    if pos < 0:
        minus_book.append(-pos)
    elif pos > 0:
        plus_book.append(pos)

minus_book.sort()
plus_book.sort()

# print(minus_book, plus_book)


def cal_range(first_array, secont_array) :
    cnt = 0
    range = 0
    while first_array :
        count = M 
        if cnt == 0 :
            range += first_array[-1]
        else :
            range += first_array[-1] * 2
        while first_array and count > 0 :
            first_array.pop()
            count -= 1
        cnt += 1
    while secont_array :
        count = M
        if cnt == 0 :
            range += secont_array[-1]
        else :
            range += secont_array[-1] * 2
        while secont_array and count > 0 :
            secont_array.pop()
            count -= 1
        cnt += 1
    return range


if not minus_book:  
    print(cal_range(plus_book, []))
elif not plus_book:  
    print(cal_range(minus_book, []))
else: 
    if minus_book[-1] > plus_book[-1]:
        print(cal_range(minus_book, plus_book))
    else:
        print(cal_range(plus_book, minus_book))