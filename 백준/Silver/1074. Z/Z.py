N, r, c = map(int, input().split())

def ans(N, r, c) :
    if N == 0 :
        return 0
    
    else :
        return 2 * (r % 2) + (c % 2) + 4 * ans(N - 1, r // 2, c // 2)
    
print(ans(N, r, c))