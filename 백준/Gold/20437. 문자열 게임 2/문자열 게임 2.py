N = int(input())

for i in range(N) :
    ans1 = 100001
    ans2 = -1
    mystring = list(input())
    K = int(input())
    alphabet = [[] for _ in range(26)]
    for j in range(len(mystring)) :
        #print(ord(mystring[j]))
        alphabet[ord(mystring[j]) - 97].append(j)

    for j in range(26) :
        if (K == 1) :
            ans1 = 0
            ans2 = 0
        else :
            if (len(alphabet[j]) >= K) :
                k = 0
                while(k + K - 1 < len(alphabet[j])) :
                    firstalp = alphabet[j][k]
                    lastalp = alphabet[j][k + K - 1]
                    diff = lastalp - firstalp
                    if(diff <= ans1) :
                        ans1 = diff
                    if(diff >= ans2) : 
                        ans2 = diff
                    k += 1

    if(ans1 == 100001 or ans2 == -1) :
        print(-1)
    else :
        print(ans1 + 1, ans2 + 1)