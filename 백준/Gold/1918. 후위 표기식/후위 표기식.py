def is_alphabet(char):
    ascii_value = ord(char)
    return (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <= 122)

mystring = input()
mystring = list(mystring)
stack = []
cnt = 0
ans = []

for s in mystring :
    if is_alphabet(s) :
        ans.append(s)
        continue
    if (s == '(' or s == ')') :
        if (s == '(') :
            stack.append(s)
        else :
            while stack :
                if(stack[-1] == '(') :
                    break
                ans.append(stack.pop())
            stack.pop()
    elif (s == '+' or s == '-') :
        while stack :
            if(stack[-1] == '(') :
                break
            ans.append(stack.pop())
        stack.append(s)
    elif (s == '*' or s == '/') :
        while stack :
            if(stack[-1] != '*' and stack[-1] != '/') :
                break
            ans.append(stack.pop())
        stack.append(s)

while stack :
    ans.append(stack.pop())

print("".join(ans))