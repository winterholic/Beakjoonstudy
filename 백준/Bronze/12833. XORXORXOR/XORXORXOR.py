A, B, C = map(int, input().split())

if C % 2 == 1 :
    C = 1
else :
    C = 2

for i in range(C) :
    A = A ^ B

print(A)