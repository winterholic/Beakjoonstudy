N, M = map(int,input().split())

str_N = str(N)
rev_N = str_N[::-1]
str_M = str(M)
rev_M = str_M[::-1]

new_N = int(rev_N)
new_M = int(rev_M)

print(max(new_N, new_M))