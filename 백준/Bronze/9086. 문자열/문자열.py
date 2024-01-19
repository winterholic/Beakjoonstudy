N = int(input())

for i in range(N):
    mystring = input()
    print(mystring[0], end = "")
    print(mystring[len(mystring) - 1])