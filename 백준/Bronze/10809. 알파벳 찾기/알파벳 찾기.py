mystring = input()

alphabet = {}

for i in range(26) :
    alphabet[i] = -1

for i in range(len(mystring)) :
    temp = ord(mystring[i]) - 97
    #print(temp)
    if(alphabet[temp] == -1) :
        alphabet[temp] = i

for i in range(26) :
    print(alphabet[i], end = " ")