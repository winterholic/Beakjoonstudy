constructor = {}

for i in range(10000) :
    constructor[i] = True

for i in range(10000) :
    number = str(i)
    sum = 0
    sum += i
    for j in range(len(number)) :
        sum += int(number[j])
    constructor[sum] = False
    
for i in range(10000) :
    if(constructor[i] == True) :
        print(i)