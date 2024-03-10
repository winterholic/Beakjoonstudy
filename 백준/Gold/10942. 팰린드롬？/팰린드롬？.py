import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int, input().split()))
n = len(s)

M = int(input())

TC = []
for i in range(M) :
    a, b = map(int, input().split())
    TC.append((a, b))

is_palindrome = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(i + 1):
        if s[i] == s[j] and (i - j < 2 or is_palindrome[j + 1][i - 1]) :
            is_palindrome[j][i] = True

# for ip in is_palindrome :
#     print(*ip)

for S, E in TC :
    if(is_palindrome[S - 1][E - 1]) :
        print(1)
    else :
        print(0)