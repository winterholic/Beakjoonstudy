def isPelindrome(N) :
    return list(str(N)) == list(str(N))[::-1]

while True :
    N = int(input())
    if N == 0 :
        break
    if isPelindrome(N) :
        print("yes")
    else :
        print("no")