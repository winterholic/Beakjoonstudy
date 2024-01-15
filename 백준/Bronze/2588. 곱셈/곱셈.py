a = int(input())
b = int(input())
c = (b//10)%10
d = (b//100)%10
print(a*(b%10))
print(a*c)
print(a*d)
print(a*b)