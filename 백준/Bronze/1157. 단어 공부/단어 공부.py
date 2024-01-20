mystring = input()

alphabet = {}

for i in range(26) :
    alpha = chr(i + 65)
    alphabet[alpha] = 0

#print(alphabet)

for i in range(len(mystring)) :
    if('a' <= mystring[i] <= 'z') :
        alphabet[chr(ord(mystring[i]) - 32)] += 1
    else :
        alphabet[mystring[i]] += 1

same_flag = 0
max = alphabet['A']
max_alphabet = 'A'

#print(alphabet)

flag = 0

for alp, cnt in alphabet.items() :
    if(flag == 0) :
        flag += 1
        continue
    if(cnt == max) :
        same_flag = 1
        continue
    if(cnt > max) :
        max = cnt
        max_alphabet = alp
        same_flag = 0

if(same_flag == 1) :
    print("?")
else :
    print(max_alphabet)