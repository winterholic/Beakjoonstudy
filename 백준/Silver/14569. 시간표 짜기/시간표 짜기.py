import sys
input = sys.stdin.readline

N = int(input())

sub = []

for i in range(N) :
    temp = list(map(int, input().split()))
    sub.append(temp[1 :])

#sub[0]에는 개수라 의미없는데이터

M = int(input())

stu = []

for i in range(M) :
    temp = list(map(int, input().split()))
    stu.append(temp[1 :])
    #stu[0]에는 개수라 의미없는데이터

for i in range(M) :
    myschedule = stu[i]
    cnt = 0
    for j in range(N) :
        flag = 1
        for k in range(len(sub[j])) :
            if not sub[j][k] in stu[i] :
                flag = 0
                break
        if flag == 1 :
            cnt += 1
    print(cnt)