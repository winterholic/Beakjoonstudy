word = input()

stack = []

for w in word :
    if "".join(stack[-4:]) == "PPAP" :
        stack.pop()
        stack.pop()
        stack.pop()
    stack.append(w)

if("".join(stack) == "PPAP" or "".join(stack) == "P") :
    print("PPAP")
else :
    print("NP")