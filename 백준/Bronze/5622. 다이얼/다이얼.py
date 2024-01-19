mystring = input()

alphabet = {}

tmp = 1
for i in range(18) :
    if(i % 3 == 0) :
        tmp += 1
    alpha = chr(i + 65)
    alphabet[alpha] = tmp

alphabet['S'] = 7
alphabet['T'] = 8
alphabet['U'] = 8
alphabet['V'] = 8
alphabet['W'] = 9
alphabet['X'] = 9
alphabet['Y'] = 9
alphabet['Z'] = 9

#print(alphabet)

Time = {1 : 2, 2 : 3, 3 : 4, 4 : 5, 5 : 6, 6 : 7, 7 : 8, 8 : 9, 9 : 10}

sum = 0

for i in range(len(mystring)) :
    num = alphabet[mystring[i]]
    sum += Time[num]

print(sum)