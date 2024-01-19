N = int(input())

for i in range(N) :
    R, S = map(str, input().split())
    R = int(R)
    for j in range(len(S)) :
        for k in range(R) :
            print(S[j], end = "")
    print()