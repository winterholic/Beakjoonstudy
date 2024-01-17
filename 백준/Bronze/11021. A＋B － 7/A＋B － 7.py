import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) :
    A, B = map(int, input().split())
    mystring = "Case #" + str(i + 1) + ":"
    print(mystring, A + B)