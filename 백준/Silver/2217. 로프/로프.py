N = int(input())

numbers = []

for i in range(N) :
    numbers.append(int(input()))

minimal = -1

numbers = sorted(numbers)

for number in numbers :
    new_data = number * N
    #print(new_data)
    N -= 1
    minimal = max(minimal, new_data)

#print("ans", minimal)
print(minimal)