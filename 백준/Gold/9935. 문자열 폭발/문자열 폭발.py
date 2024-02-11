A = input()
B = input()

"""while (B in A) :
    result = A.replace(B, "")
    A = result

if (len(A) == 0) :
    print("FRULA")
else :
    print(A)"""

lenB = len(B)
stack = []

for a in A :
    stack.append(a)
    if ''.join(stack[-len(B):]) == B :
        for _ in range(lenB) :
            stack.pop()

result = ''.join(stack)
if(len(result) > 0) :
    print(result)
else :
    print("FRULA")