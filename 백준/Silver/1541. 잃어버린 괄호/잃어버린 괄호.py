formula = input().split('-')

#print(formula)
answer = 0

i = 0
for number in formula :
    temps = number.split('+')
    #print(temps)
    if i == 0 :
        sum = 0
        for temp in temps :
            sum += int(temp)
        answer += sum
        i += 1
    else :
        sum = 0
        for temp in temps :
            sum += int(temp)
        answer -= sum

print(answer)