from math import comb

N, M, K = map(int, input().split())

mystring = ''

result = comb(N + M, N)

if(result < K) :
    print(-1)
else :
    while (K > 0) and (N > 0) and (M > 0):
        zflag = comb(N + M - 1, N - 1)
        #print(K, zflag, "N = ", N, "M = ", M)
        if K > zflag :
            K -= zflag
            M -= 1
            mystring += 'z'
        else :
            N -= 1
            mystring += 'a'
    for i in range(N) :
        mystring += 'a'
    for i in range(M) :
        mystring += 'z'

    print(mystring)